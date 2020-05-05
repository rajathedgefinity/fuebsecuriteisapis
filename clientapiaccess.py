import requests

url = 'http://127.0.0.1:8000/api/hello/'
headers = {'Authorization': 'Token 9095e00d75738c2762419ab23148d0a073c54c51'}
r = requests.get(url, headers=headers)
print(r.text)
