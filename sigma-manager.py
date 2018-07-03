#!/usr/bin/env python3
## sigma-manager
## Soumille Lucas
## 02/07/2018

import shutil

from sigma_manager.GitManager import GitManager
from sigma_manager.Sigma import SigmaWrapper
from sigma_manager.FolderHelper import FolderHelper
from sigma_manager.Constants import *

class SigmaManager():

	gm_sigma_rules = None
	gm_sigma_configurtion = None
	gm_elastalert_rules = None

	def init_git_repositories(self):
		print("# Pull ITER Sigma rules repository #")
		#delete already existing repository
		shutil.rmtree(RULE_PATH, ignore_errors=True)
		self.gm_sigma_rules = GitManager(GIT_PROTOCOL, ITER_SIGMA_RULE_REPOSITORY, RULE_PATH)
		self.gm_sigma_rules.clone_repository()
		print("# Pull ITER Sigma Configuration repository #")
		shutil.rmtree(CONFIGURATION_PATH, ignore_errors=True)
		self.gm_sigma_rules = GitManager(GIT_PROTOCOL, ITER_CONFIGURATION_REPOSITORY, CONFIGURATION_PATH)
		self.gm_sigma_rules.clone_repository()
		print("# Init ITER Elastalert rule repository #")
		shutil.rmtree(DESTINATION_PATH, ignore_errors=True)
		#TO BE UPDATED
		self.gm_elastalert_rules = GitManager(GIT_PROTOCOL, ITER_CONFIGURATION_REPOSITORY, CONFIGURATION_PATH)

	def convert_rules(self):
		print("# Load all sigma rules #")
		#fh = FolderHelper()
		sw = SigmaWrapper(FolderHelper.get_all_yaml_files(RULE_PATH))
		sw.process_rules()

	def run(self):
		print("# Start sigma-manager tool #")
		print("# Step 1 : Pull Rules and Config #")
		self.init_git_repositories()
		print("# Step 2 : Convert Sigma rules to Elastalert #")
		self.convert_rules()

if __name__== "__main__":
	SigmaManager().run()