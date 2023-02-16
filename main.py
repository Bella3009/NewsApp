import requests

#newsapi.org
api_key = "d16abece8b5446b698fbbab95c443604"
topic = input("What topic you wish to see: ")
lang = input("Choose language: en or it ")
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-01-16&sortBy=publishedAt&apiKey={api_key}&language={lang}"

r = requests.get(url)
content = r.json()

for article in content['articles']:
    print(article['title'])
    print(article['description'])
