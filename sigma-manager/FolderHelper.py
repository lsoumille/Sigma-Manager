## FolderHelper
## Soumille Lucas
## 02/07/2018

import os
import sys

class FolderHelper():

	def __init__(self, rootdir):
		self.rootdir = rootdir

	def get_all_yaml_files(self):
		for root, subdirs, files in os.walk(self.rootdir):
			print("root " + str(root))
			print("subdirs " + str(subdirs))
			print("files " + str(files))