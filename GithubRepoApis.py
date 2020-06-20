import requests
import os
from urllib.parse import urljoin
import constans
from constans import Github

Github.BASE_URL,Github.SEARCH,Github.CODE

class GitRepositoryApisDetails:

    def search_repository_details(self,repo_name):



        self.target_url = "{BASE_URL}/{SEARCH}/{CODE}".format(BASE_URL=Github.BASE_URL.value,
                                                              SEARCH=Github.SEARCH.value,
                                                              CODE=Github.CODE.value)

        self.query_string = "?q={}".format(repo_name)

        self.query_url = "{}{}".format(self.target_url , self.query_string)

        #self.url = 'https://api.github.com/search/repositories?q=dockerfile'

        headers = {'content-type': 'application/json'}

        self.response = requests.get(self.query_url, headers=headers)

        self.response.raise_for_status()

        self.matched_repositories = self.response.json()

        result = []
        for repo in self.matched_repositories["items"]:

            repo_details = dict()
            repo_details["id"] = repo.get("id")
            repo_details["name"] = repo.get("name")
            repo_details["full_name"] = repo.get("full_name")
            repo_details["private"] = repo.get("private")
            repo_details["owner"] = dict()
            repo_details["owner"]["login"] = repo.get("login")
            repo_details["owner"]["id"] = repo.get("id")
            repo_details["owner"]["html_url"] = repo.get("html_url")
            repo_details["html_url"] = repo.get("html_url")
            repo_details["description"] = repo.get("description")
            repo_details["url"] = repo.get("url")
            repo_details["contents_url"] = repo.get("contents_url")
            repo_details["created_at"] = repo.get("created_at")
            repo_details["updated_at"] = repo.get("updated_at")

            if repo.get("license"):
                repo_details["license"] = dict()
                repo_details["license"]["key"] = repo.get("key")
                repo_details["license"]["name"] = repo.get("name")
                repo_details["license"]["spdx_id"] = repo.get("spdx_id")
                repo_details["license"]["url"] = repo.get("url")

            repo_details["forks"] = repo.get("forks")
            repo_details["watchers"] = repo.get("watchers")

            print(repo_details)
            result.append(repo_details)

        return (result)

find_repo = GitRepositoryApisDetails()

total_result = find_repo.search_repository_details("dockerfile")
print(total_result)
