import requests

x = requests.get('https://api.github.com/repositories')
x = x.json()
print(x)