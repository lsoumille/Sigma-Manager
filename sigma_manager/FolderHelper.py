## FolderHelper
## Soumille Lucas
## 02/07/2018

import os
import sys
import yaml
import shutil

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

	def load_yaml_dict(rootdir):
		dict_from_file = {}
		if os.path.exists(rootdir):
			with open(rootdir) as f:
				dict_from_file = yaml.load(f.read())
		return dict_from_file

	def load_alert_profiles(alert_profile_path):
		alert_profile = {}
		for root, subdirs, files in os.walk(alert_profile_path):
			for file in files:
				backend_options = []
				with open(os.path.join(root, file)) as f:
					lines = f.readlines()
					for line in lines:
						backend_options.append(line.rstrip())
				alert_profile[file] = backend_options
		return alert_profile

	def write_line_to_file(line, file_path):
		with open(file_path, 'a+') as f:
			f.write(line + "\n")

	def copy_file(src_path, dest_path):
		shutil.copyfile(src_path, dest_path)

	def delete_folder_content(rootdir):
		shutil.rmtree(rootdir, ignore_errors=True)


