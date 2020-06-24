import requests
from constans import Github

class GitRepositoryApisDetails:

    def search_repository_details(self,repo_name):

        self.target_url = "{BASE_URL}/{SEARCH}/{REPOSITORIES}".format(BASE_URL=Github.BASE_URL.value,
                                                              SEARCH=Github.SEARCH.value,
                                                              REPOSITORIES=Github.REPOSITORIES.value)
        self.query_string = "?q={}".format(repo_name)
        self.query_url = "{}{}".format(self.target_url,self.query_string)
        headers = {'content-type': 'application/json'}
        self.response = requests.get(self.query_url, headers=headers)
        self.matched_repositories = self.response.json()

        all_repositories_details = []
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
            all_repositories_details.append(repo_details)

        return (all_repositories_details)


