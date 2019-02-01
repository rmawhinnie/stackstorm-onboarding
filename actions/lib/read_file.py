from st2actions.runners.pythonrunner import Action
from github import Github
import json
import yaml

class Get(Action):
    def run(self, github_url, user_name, password, repo_name, file_name):
        github = Github(base_url=github_url, login_or_token=user_name, password=password)
        repo = github.get_repo(repo_name)
        doc = repo.get_contents(file_name)
        return yaml.load(doc.decoded_content)
