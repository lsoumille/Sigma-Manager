## FolderHelper
## Soumille Lucas
## 02/07/2018

import os
import sys
import yaml

class FolderHelper():

	def get_all_yaml_files(rootdir):
		files_dict = {}
		for root, subdirs, files in os.walk(rootdir):
			#Ietrate through files
			for file in files:
				#If it's not a yml file continue
				if not file.endswith(".yml"):
					continue
				filename = file[:-4]
				filename_path = os.path.join(root, file)
				files_dict[filename] = filename_path
		return files_dict

	def create_folder(folder_path):
		os.makedirs(folder_path, exist_ok=True)

	def load_alert_configuration(alert_conf_path):
		alert_dict = {}
		if os.path.exists(alert_conf_path):
			with open(alert_conf_path) as f:
				alert_dict = yaml.load(f.read())
		return alert_dict

	def load_alert_profiles(alert_profile_path):
		alert_profile = {}
		for root, subdirs, files in os.walk(alert_profile_path):
			for file in files:
				backend_options = []
				with open(os.path.join(root, file)) as f:
					lines = f.readlines()
					for line in lines:
						backend_options.append(line)
				alert_profile[file] = backend_options
		return alert_profile

	def write_line_to_file(line, file_path):
		with open(file_path, 'a+') as f:
			f.write(line + "\n")	

