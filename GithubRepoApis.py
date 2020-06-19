import requests


class GitRepositoryApisDetails:

    def search_repository_details(self):
        self.url = 'https://api.github.com/search/repositories?q=dockerfile'
        headers = {'content-type': 'application/json'}
        self.response = requests.get(self.url, headers=headers)
        self.response.raise_for_status()
        self.jsonResponse = self.response.json()

        result = []
        for repo in self.jsonResponse["items"]:
            dict1 = {}
            dict2 = {}
            dict3 = {}
            dict1.update({'id': repo["id"],
                      'name': repo["name"],
                      'full_name': repo["full_name"],
                      'private': repo["private"],
                      'login': repo["owner"]["login"],
                      'id': repo["owner"]["id"],
                      'html_url': repo["owner"]["html_url"],
                      'html_url': repo["html_url"],
                      'description': repo["description"],
                      'url': repo["url"],
                      'contents_url': repo["contents_url"],
                      'created_at': repo["created_at"],
                      'updated_at': repo["updated_at"]})

            if repo.get('license')!=None:

                dict2.update({'key': repo["license"]["key"],
                          'name':repo["license"]["name"],
                          'spdx_id':repo["license"]["spdx_id"],
                          'url':repo["license"]["url"]})
                dict1.update(dict2)
            dict3.update({'forks': repo["forks"],
                      'watchers': repo["watchers"]})
            dict1.update(dict3)

            result.append(dict1)

        return (result)

find_repo = GitRepositoryApisDetails()

total_result = find_repo.search_repository_details()
print(total_result)
