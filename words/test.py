import requests

r = requests.get("http://www.google.com",
                 proxies={"http": "http://depprxy.ds.dep.nycnet:8080"})
print(r.text)