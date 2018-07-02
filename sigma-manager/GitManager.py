## Git Manager
## Soumille Lucas
import git
import os

from git import Repo

class GitManager():

	def __init__(self, repository_type, repository_url, repository_path):
		self.type = repository_type
		self.url = repository_url
		self.path = repository_path

	def clone_repository(self):
		Repo.clone_from(self.url, self.path)

	def push_repository(self):
		git_repo = Repo(self.path)
		git_repo.git.add('-A')
		git_repo.git.commit(m='Commit from Python script')
		git_repo.git.push('--set-upstream', 'origin', 'master')

