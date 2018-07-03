## Sigma
## Soumille Lucas
## 03/07/2018

import yaml
import os
import subprocess

from sigma_manager.Constants import *
from sigma_manager.FolderHelper import FolderHelper

class SigmaWrapper():

	#Rule dict is a dictionary with rulename as keys and rule path as values
	def __init__(self, rule_dict):
		self.rule_dict = rule_dict
		#Load Alert configuration
		alert_conf_path = os.path.join(CONFIGURATION_PATH, CONFIGURATION_ALERT_FILENAME)
		self.alert_dict = FolderHelper.load_alert_configuration(alert_conf_path)
		#Load alert profile
		alert_profile_path = os.path.join(CONFIGURATION_PATH, CONFIGURATION_ALERT_PROFILES)
		self.alert_profiles = FolderHelper.load_alert_profiles(alert_profile_path)

	def generate_sigma_query(self, rule_path, backend_options):
		sigma_cmd = ['sigmac', '-t', SIGMA_BACKEND, rule_path]
		for opt in backend_options:
			sigma_cmd.append('--backend-option')
			sigma_cmd.append(opt)
		return sigma_cmd

	def process_rules(self):
		for rule_name, rule_path in self.rule_dict.items():
			#Check if a rule has a dedicated alert profile
			if rule_name in self.alert_dict:
				backend_options = self.alert_profiles[self.alert_dict[rule_name]]
			else:
				backend_options = self.alert_profiles[DEFAULT_ALERT_PROFILE]
			
			target_rule_path = rule_path.replace(RULE_PATH, DESTINATION_PATH)
			target_folder_path = os.path.dirname(target_rule_path)
			#Create directory in target path
			FolderHelper.create_folder(target_folder_path)
			#Call sigmac
			sigma_result = subprocess.check_output(self.generate_sigma_query(rule_path, backend_options))
			#Write in files
			rule_number = 0
			for line in sigma_result.decode('utf-8').splitlines():
				#In case of one sigma rule generates several elastalert rule
				if not line:
					rule_number = rule_number + 1
					continue
				file_path = os.path.join(target_folder_path, rule_name) + "_" + str(rule_number) + ".yml"
				FolderHelper.write_line_to_file(str(line), file_path)