import requests

def load_url (url, token):
    return requests.get('http://localhost:5000' + url, headers={'X-Access-Token': token}).json()

access_token = load_url('/register', '')['access_token']
access_home = load_url('/home', access_token)['link']
