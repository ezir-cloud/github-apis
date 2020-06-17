import requests

class RepositoryDetails:

    def search_repository(self):
        self.url = 'https://api.github.com/search/repositories?q=java'
        headers = {'content-type': 'application/json'}
        self.r = requests.get(self.url, headers=headers)
        print(self.r.text)


find_repo = RepositoryDetails()
find_repo.search_repository()

























