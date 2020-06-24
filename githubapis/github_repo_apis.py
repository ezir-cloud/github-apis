import requests
from githubapis.constants import Github


class GithubRepoApis:

    def get_matched_files_in_repo_by_file_name(self,repo_name,file_name):
        self.target_url = "{BASE_URL}/{SEARCH}/{CODE}".format(BASE_URL=Github.BASE_URL.value,
                                                              SEARCH=Github.SEARCH.value,
                                                              CODE=Github.CODE.value)
        self.query_string ="?q=repo:{}+filename:{}".format(repo_name,file_name)
        self.query_url = "{}{}".format(self.target_url, self.query_string)
        headers = {'content-type': 'application/json'}
        self.response = requests.get(self.query_url, headers=headers)
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
        return all_file_details
