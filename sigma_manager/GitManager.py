## Git Manager
## Soumille Lucas
## 02/07/2018

import git

from git import Repo
from sigma_manager.FolderHelper import FolderHelper

class GitManager():

	def __init__(self, repository_type, repository_url, repository_path, repository_branch='master'):
		self.type = repository_type
		self.url = repository_url
		self.path = repository_path
		self.branch = repository_branch

	#Clone repository URL into Repository Path 
	def clone_repository(self):
		Repo.clone_from(self.url, self.path, branch=self.branch)

	def clone_and_flush(self):
		Repo.clone_from(self.url, self.path, branch=self.branch)
		FolderHelper.delete_visible_content(self.path)

	#Push repository path to repository URL 
	def push_repository(self):
		try:
			git_repo = Repo(self.path)
			git_repo.git.add('-A')
			git_repo.git.commit(m='Commit from Python script')
			git_repo.git.push('--set-upstream', 'origin', self.branch)
		except git.exc.GitCommandError as err:
			if "Your branch is up to date" in str(err) or "nothing to commit" in str(err):
				print("# Ruleset is already up to date #")
			else:
				raise	
			
