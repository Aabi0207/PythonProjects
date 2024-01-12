from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/")
# yc_webpage = response.text
#
# with open("hacker_news_source_code.txt", "w") as data:
#     data.write(yc_webpage)
with open("hacker_news_source_code.txt") as data:
    source_code = data.read()

soup = BeautifulSoup(source_code, "html.parser")
# print(soup.title)

article_texts = []
article_links = []
headlines = soup.find_all(name="a", rel="noreferrer")
for tag in headlines:
    article_texts.append(tag.get_text())
    article_links.append(tag.get("href"))

article_upvote = soup.find_all(name="span", class_="score")
article_upvotes = [int(i.get_text().split()[0]) for i in article_upvote]

# print(article_texts[0])
# print(article_links[0])
# print(article_upvotes[0])

highest_votes = max(article_upvotes)
highest_voted_article = article_texts[article_upvotes.index(highest_votes)]
highest_voted_article_link = article_links[article_upvotes.index(highest_votes)]

print(highest_votes)
print(highest_voted_article)
print(highest_voted_article_link)