import requests

def get_random_wiki_title():
    params = {
        "action": "query",
        "format": "json",
        "list": "random",
        "rnnamespace": 0,
        "rnlimit": 1
    }
    response = do_request(params)
    response.raise_for_status()

    title = response.json()["query"]["random"][0]

    return title["title"]

def get_detailed_wiki(title):
    params = {
        "action": "parse",
        "page": title,
        "prop": "text",
        "format": "json"
    }
    response = do_request(params)
    response.raise_for_status()

    data = response.json()["parse"]["text"]

    return data

def do_request(params):
    url = "https://en.wikipedia.org/w/api.php"
    headers = {"User-Agent": "smarter/0.1"}
    return requests.get(url, params=params, headers=headers)