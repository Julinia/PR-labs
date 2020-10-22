import requests
import concurrent.futures

def load_url (url, token):
    return requests.get('http://localhost:5000' + url, headers={'X-Access-Token': token}).json()

access_token = load_url('/register', '')['access_token']
access_home = load_url('/home', access_token)['link']

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    links = access_home
    future_to_url = {executor.submit(load_url, links[key], access_token): key for key in links}
    for future in concurrent.futures.as_completed(future_to_url):
        key = future_to_url[future]
        data = future.result()
        print(data)