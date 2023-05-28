import requests
from send_email import send_email

#newsapi.org
api_key = "d16abece8b5446b698fbbab95c443604"
topic = input("What topic you wish to see: ")

url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

# Making the request
r = requests.get(url)
content = r.json()
body = ""

# Retrieve the data
for article in content['articles'][:20]:
    if article["title"] is not None:
        body = body + article['title'] + "\n" + article['description'] + "\n" + article['url'] + 2*"\n"

# Add also a subject to the email.
message = f"""\
Subject: News titles

{body}
"""

message = message.encode("utf-8")
send_email(message)
