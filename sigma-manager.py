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
		FolderHelper.delete_folder_content(RULE_PATH)
		self.gm_sigma_rules = GitManager(GIT_PROTOCOL, ITER_SIGMA_RULE_REPOSITORY, RULE_PATH)
		self.gm_sigma_rules.clone_repository()
		print("# Pull ITER Sigma Configuration repository #")
		FolderHelper.delete_folder_content(CONFIGURATION_PATH)
		self.gm_sigma_rules = GitManager(GIT_PROTOCOL, ITER_CONFIGURATION_REPOSITORY, CONFIGURATION_PATH)
		self.gm_sigma_rules.clone_repository()
		print("# Init ITER Elastalert rule repositories #")
		FolderHelper.delete_folder_content(DESTINATION_PATH_1)
		self.gm_elastalert_rules_1 = GitManager(GIT_PROTOCOL, ITER_ELASTALERT_REPOSITORY, DESTINATION_PATH_1, ITER_ELASTALERT_REPOSITORY_BRANCH_1)
		self.gm_elastalert_rules_1.clone_and_flush()
		FolderHelper.delete_folder_content(DESTINATION_PATH_2)
		self.gm_elastalert_rules_2 = GitManager(GIT_PROTOCOL, ITER_ELASTALERT_REPOSITORY, DESTINATION_PATH_2, ITER_ELASTALERT_REPOSITORY_BRANCH_2)
		self.gm_elastalert_rules_2.clone_and_flush()
		
	def convert_rules(self):
		print("# Load all sigma rules #")
		sw = SigmaWrapper(FolderHelper.get_all_yaml_files(RULE_PATH))
		print("# Start Sigma to Elastalert #")
		sw.process_rules()
		print("# Elastalert rules created #")

	def push_ruleset(self):
		self.gm_elastalert_rules_1.push_repository()
		self.gm_elastalert_rules_2.push_repository()

	def run(self):
		print("# Start sigma-manager tool #")
		print("# Step 1 : Pull Rules and Config #")
		self.init_git_repositories()
		print("# Step 2 : Convert Sigma rules to Elastalert #")
		self.convert_rules()
		print("# Step 3 : Push Ruleset #")
		self.push_ruleset()
		print("# Sigma-manager tool successful execution #")

if __name__== "__main__":
	SigmaManager().run()