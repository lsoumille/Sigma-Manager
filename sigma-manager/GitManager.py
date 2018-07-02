## Git Manager
## Soumille Lucas
## 02/07/2018

import git
import os

from git import Repo

class GitManager():

	def __init__(self, repository_type, repository_url, repository_path):
		self.type = repository_type
		self.url = repository_url
		self.path = repository_path

	#Clone repository URL into Repository Path 
	def clone_repository(self):
		Repo.clone_from(self.url, self.path)

	#Push repository path to repository URL
	def push_repository(self):
		git_repo = Repo(self.path)
		git_repo.git.add('-A')
		git_repo.git.commit(m='Commit from Python script')
		git_repo.git.push('--set-upstream', 'origin', 'master')

