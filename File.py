import  requests

class File:

    def search_file(self):

     self.url = 'https://api.github.com/search/code?q=repo:mritd/dockerfile+filename:dockerfile'
     headers = {'content-type': 'application/json'}
     self.r = requests.get(self.url, headers=headers)
     print (self.r.text)
obj = File()
obj.search_file()


