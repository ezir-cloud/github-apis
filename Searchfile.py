import  requests

url = 'https://api.github.com/search/code?q=repo:mritd/dockerfile+filename:dockerfile'
headers = {'content-type': 'application/json'}
r = requests.get(url, headers=headers)
print (r.text)