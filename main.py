import requests
#from send_email import send_email

#newsapi.org
api_key = "d16abece8b5446b698fbbab95c443604"
topic = input("What topic you wish to see: ")
lang = input("Choose language: en or it ")
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-02-16&sortBy=publishedAt&apiKey={api_key}&language={lang}"

r = requests.get(url)
content = r.json()
body = ""

for article in content['articles'][:20]:
    if article["title"] is not None:
        body = body + article['title'] + "\n" + article['description'] + + "\n" + article['url'] (2*"\n")
    
body = body.encode("utf-8")
#send_email(body)
