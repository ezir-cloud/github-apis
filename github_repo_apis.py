"""display items are  name "name": "Dockerfile", "path": "radicale/Dockerfile",
"url": "https://api.github.com/repositories/66067220/contents/radicale/Dockerfile?
ref=ed9c7f50cb619ebcca955e283e8ec66bc3d4cb39", "git_url":
"https://api.github.com/repositories/66067220/git/blobs/e7da19f10da60a2633fa8e82cd77c4760ee1afc1","html_url":
"https://github.com/mritd/dockerfile/blob/ed9c7f50cb619ebcca955e283e8ec66bc3d4cb39/radicale/Dockerfile","owner": {
"owner":"mritd","id": 13043245,"url": https://api.github.com/users/mritd", "html_url": "https://github.com/mritd"
"""

import requests
import os
import constans
from constans import Github

Github.BASE_URL, Github.SEARCH, Github.CODE
class GithubRepoApis:
    base_url = os.path.join(Github.BASE_URL.value, Github.SEARCH.value, Github.CODE.value)

    def get_matched_files_in_repo_by_file_name(self, repo_name, file_name):
        self.query_string = "?q=repo:{}+filename:{}".format(repo_name, file_name)
        self.query_url = "{}{}".format(self.base_url, self.query_string)
        print(self.query_url)
        headers = {'content-type': 'application/json'}
        self.response = requests.get(self.query_url, headers=headers)
        # access JSON content using json().
        self.matched_files = self.response.json()
        all_file_details = []

        for file_details in self.matched_files["items"]:
            required_file_details = dict()
            required_file_details["name"] = file_details.get("name")
            required_file_details["path"] = file_details.get("path")
            required_file_details["url"] = file_details.get("url")
            required_file_details["git_url"] = file_details.get("git_url")
            required_file_details["html_url"] = file_details.get("html_url")
            required_file_details["owner"] = dict()
            required_file_details["owner"]["login"] = file_details.get("repository").get("owner").get("login")
            required_file_details["owner"]["id"] = file_details.get("repository").get("owner").get("id")
            required_file_details["owner"]["url"] = file_details.get("repository").get("owner").get("url")
            required_file_details["owner"]["html_url"] = file_details.get("repository").get("owner").get("html_url")


            all_file_details.append(required_file_details)
            return required_file_details
Dockerfile = GithubRepoApis()
result = Dockerfile.get_matched_files_in_repo_by_file_name("mritd/dockerfile", "dockerfile")
print(result)
