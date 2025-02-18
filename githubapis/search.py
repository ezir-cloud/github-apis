import requests
from githubapis.constants import Github


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
            repo_details["repo_name"] = repo.get("name")
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

        return all_repositories_details


class GithubRepoApis:


    def get_matched_files_in_repo_by_file_name(self, repo_name, file_name):
        self.target_url = "{BASE_URL}/{SEARCH}/{CODE}".format(BASE_URL=Github.BASE_URL.value,
                                                              SEARCH=Github.SEARCH.value,
                                                              CODE=Github.CODE.value)

        self.query_string = "?q=repo:{}+filename:{}".format(repo_name, file_name)
        self.query_url = "{}{}".format(self.target_url, self.query_string)
        headers = {'content-type': 'application/json'}
        self.response = requests.get(self.query_url, headers=headers)
        self.matched_files = self.response.json()

        all_file_details = []
        for file_details in self.matched_files["items"]:
            required_file_details = dict()
            file_details_url = file_details.get("url")
            file_info= self.show_file_content(file_details_url)
            required_file_details.update(file_info)
            required_file_details["owner"] = dict()
            required_file_details["owner"]["login"] = file_details.get("repository").get("owner").get("login")
            required_file_details["owner"]["id"] = file_details.get("repository").get("owner").get("id")
            required_file_details["owner"]["url"] = file_details.get("repository").get("owner").get("url")
            required_file_details["owner"]["html_url"] = file_details.get("repository").get("owner").get("html_url")
            all_file_details.append(required_file_details)

        return all_file_details

    def show_file_content(self, file_info_url):

        self.file_url_reponse = requests.get(file_info_url)
        self.file_url_content = self.file_url_reponse.json()

        file_content_details = dict()
        file_content_details["file_name"] = self.file_url_content.get("name")
        file_content_details["path"] = self.file_url_content.get("path")
        file_content_details["sha"] = self.file_url_content.get("sha")
        file_content_details["size"] = self.file_url_content.get("size")
        file_content_details["url"] = self.file_url_content.get("url")
        file_content_details["html_url"] = self.file_url_content.get("html_url")
        file_content_details["git_url"] = self.file_url_content.get("git_url")
        file_content_details["download_url"] = self.file_url_content.get("download_url")
        file_content_details["type"] = self.file_url_content.get("type")
        file_content_details["encoding"] = self.file_url_content.get("encoding")

        return  file_content_details