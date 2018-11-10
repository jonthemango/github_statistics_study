import requests


def githubRequest(req):
    try:
        from config import oauth
        oauth = "?access_token=" + oauth
        return requests.get(req + oauth).json()
    except:
        return dict()


def getRandomRepo():
    pass

x = githubRequest('https://api.github.com/')

