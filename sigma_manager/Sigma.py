## Sigma
## Soumille Lucas
## 03/07/2018

import os
import subprocess
import sys

from sigma_manager.Constants import *
from sigma_manager.FolderHelper import FolderHelper

class SigmaWrapper():

	#Rule dict is a dictionary with rulename as keys and rule path as values
	def __init__(self, rule_dict):
		self.rule_dict = rule_dict
		#Load Alert configuration
		alert_conf_path = os.path.join(CONFIGURATION_PATH, CONFIGURATION_ALERT_FILENAME)
		self.alert_dict = FolderHelper.load_yaml_dict(alert_conf_path)
		#Load Alert profile
		alert_profile_path = os.path.join(CONFIGURATION_PATH, CONFIGURATION_ALERT_PROFILES)
		self.alert_profiles = FolderHelper.load_alert_profiles(alert_profile_path)
		#Load ignore configuration
		ignore_conf_path = os.path.join(CONFIGURATION_PATH, CONFIGURATION_IGNORE_SIGMA)
		self.ignore_rule = FolderHelper.load_yaml_dict(ignore_conf_path)

	def generate_sigma_query(self, rule_path, backend_options):
		mapping_file_path = os.path.join(CONFIGURATION_PATH, CONFIGURATION_BINDING_FILENAME)
		sigma_cmd = ['sigmac', '-t', SIGMA_BACKEND, rule_path, '--config', mapping_file_path]
		for opt in backend_options:
			sigma_cmd.append('--backend-option')
			sigma_cmd.append(opt)
		return sigma_cmd

	def process_rules(self):
		for rule_name, rule_path in self.rule_dict.items():
			target_rule_path = rule_path.replace(RULE_PATH, DESTINATION_PATH)
			target_folder_path = os.path.dirname(target_rule_path)
			#Create directory in target path
			FolderHelper.create_folder(target_folder_path)
			#If the rule is not blacklisted or must be converter to sigma
			if not rule_name in self.ignore_rule or self.ignore_rule[rule_name] != IGNORE_SIGMA_VALUE:
				#Check if a rule has a dedicated alert profile
				if rule_name in self.alert_dict:
					backend_options = self.alert_profiles[self.alert_dict[rule_name]]
				else:
					backend_options = self.alert_profiles[DEFAULT_ALERT_PROFILE]
				try:
					#Call sigmac
					sigma_result = subprocess.check_output(self.generate_sigma_query(rule_path, backend_options))
				except subprocess.CalledProcessError:
					print("!!! Error during Sigmac call for rule {0} !!!".format(rule_name))
					print("!!! Ruleset was not updated !!!".format(rule_name))
					FolderHelper.delete_folder_content(DESTINATION_PATH)
					sys.exit(1)

				#Write in files
				rule_number = 0
				for line in sigma_result.decode('utf-8').splitlines():
					#In case of one sigma rule generates several elastalert rule
					if not line:
						rule_number = rule_number + 1
						continue
					file_path = os.path.join(target_folder_path, rule_name) + "_" + str(rule_number) + ".yml"
					FolderHelper.write_line_to_file(str(line), file_path)
				print("# Sigmac success for rule {0} #".format(rule_name))
			elif self.ignore_rule[rule_name] == IGNORE_SIGMA_VALUE:
				print(rule_name)
				#Copy Elastalert rule to target
				FolderHelper.copy_file(rule_path, target_rule_path)