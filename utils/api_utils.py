import requests

def make_get_request(endpoint):
    url = f"https://api.todoly.com{endpoint}"
    response = requests.get(url)
    return response
