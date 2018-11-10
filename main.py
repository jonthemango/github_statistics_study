# -*- coding: UTF-8 -*-
import requests
import random
import json

'''
1. The script queries a random project and determines the size of the project. Verify the project id in not already in the sample data set (to preserve independence)
2. If the project meets the size criteria of a large software project they our added to our sample data set.
3. Continue until N projects are inserted into the sample data set.
4. For each project in the sample data set check its most prominent language.
6. Take that language and check whether statically typed or dynamically typed.
7. Insert the project information into its corresponding data set.
8. The script calculates the sample mean, sample median, sample variance and sample standard deviation.
'''

def githubRequest(req):
    try:
        from config import oauth
        oauth = "&access_token=" + oauth
        request = req + oauth
        return requests.get(request).json()
    except Exception as e:
        return str(e)

# https://api.github.com/repositories?since=364
def getRandomRepo():
    id_of_this_repo = 156947808
    random_repo_id = random.randint(1,id_of_this_repo)
    request = "https://api.github.com/repositories?since=" + str(random_repo_id)
    x = githubRequest(request)
    return x

def isRepoLargeEnough(repo):
    pass

def getLanguages(repo):
    # 'languages_url'
    pass




x = getRandomRepo()
print(x)


