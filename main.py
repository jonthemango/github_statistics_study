# -*- coding: UTF-8 -*-
import requests
import random
import pprint
import json
dump = pprint.PrettyPrinter(indent=4).pprint
'''
1. The script queries a random project and determines the size of the project. Verify the project id in not already in the sample data set (to preserve independence)
2. If the project meets the size criteria of a large software project they our added to our sample data set.
3. Continue until N projects are inserted into the sample data set.
4. For each project in the sample data set check its most prominent language.
6. Take that language and check whether statically typed or dynamically typed.
7. Insert the project information into its corresponding data set.
8. The script calculates the sample mean, sample median, sample variance and sample standard deviation.
'''


def githubRequest(req, params={}):
    try:
        from config import oauth
        params["access_token"] = oauth    
        return requests.get(req, params=params).json()
    except Exception as e:
        return str(e)

def getRandomRepo():
    while True:
        id_of_this_repo = 156947808
        random_repo_id = random.randint(1,id_of_this_repo)
        request = "https://api.github.com/repositories/" + str(random_repo_id)
        res = githubRequest(request)

        if "message" not in res:
            return res
        elif res["message"] == "Bad credentials": # 
            raise Exception("Bad Credentials Exception")
        elif res['message'] == "Not Found": # keep going 
            continue
        elif res['message'] == "Repository access blocked":
            continue
        else:
            print(res['message'])
            raise Exception("Unknown error.")


def getLanguages(repo):
    langs = githubRequest(repo["languages_url"])
    total_bytes = 0

    prominant_lang = ''
    prominant_lang_bytes = 0
    for key in langs:
        noBytes = langs[key]
        total_bytes += noBytes
        if max(prominant_lang_bytes, noBytes) == noBytes:
            prominant_lang = key
            prominant_lang_bytes = noBytes
    return langs, total_bytes, prominant_lang

def getNumberOfContributors(repo):
    contributors = githubRequest(repo["contributors_url"])
    return len(contributors)

def isLargeEnough(bytesL, C):
    return bytesL > 1000000 and C > 10

def getLargeProject():
    isNotLargeEnough = True
    while isNotLargeEnough:
        random_repo = getRandomRepo()
        langs = getLanguages(random_repo)
        repo_obj = {
            "id" : random_repo['id'],
            "langs": langs[0],
            "total_size": langs[1],
            "prominant_lang": langs[2],
            "contributors": getNumberOfContributors(random_repo)
        }
        if isLargeEnough(repo_obj["total_size"], repo_obj["contributors"]):
            isNotLargeEnough = False
    print(repo_obj['total_size'])
    return repo_obj

def loadJsonFile(fn):
    with open(fn) as json_data:
        d = json.load(json_data)
        json_data.close()
        return d

def writeJsonFile(fn, data):
    with open(fn, 'w') as outfile:
        json.dump(data, outfile)


def main(DEFAULT=50):
    sample_data_set = {}
    explicit_data_set = {}
    implicit_data_set = {}

    langs_json = loadJsonFile("language_data/language_types.json")

    while len(sample_data_set) < DEFAULT:
        try:
            repo_obj = getLargeProject()
            print(1)
        except Exception as e:
            writeJsonFile("reports/sample_data.json", sample_data_set)
            writeJsonFile("reports/implicit_data.json", implicit_data_set)
            writeJsonFile("reports/explicit_data.json", explicit_data_set)
            input('file written')
        # declare variables
        id = repo_obj['id']
        langs = repo_obj['langs']
        prominent_lang = repo_obj['prominant_lang']


        if repo_obj['id'] in sample_data_set or langs == {} or prominent_lang not in langs_json:
            # Preserve Independance 
            # exclude projects with no programming languages
            # exclude languages not defined
            continue
        elif langs_json[prominent_lang] == "":
            # If language is defined but empty then ignore, type of lang is unknown 
            continue
        else:
            #dump("===START===")
            #dump(repo_obj)
            #dump("===END===")
            pass
        
        # Insert the repo into our sample data set
        sample_data_set[id] = repo_obj  

        
        if langs_json[prominent_lang] == "explicit":
            explicit_data_set[id] = repo_obj
        elif langs_json[prominent_lang] == "implicit":
            implicit_data_set[id] = repo_obj
    writeJsonFile("reports/sample_data.json", sample_data_set)
    writeJsonFile("reports/implicit_data.json", implicit_data_set)
    writeJsonFile("reports/explicit_data.json", explicit_data_set)


if __name__ == '__main__':
    main(50)