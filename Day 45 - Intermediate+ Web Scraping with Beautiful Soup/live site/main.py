from bs4 import BeautifulSoup
import requests as req
res = req.get('https://news.ycombinator.com/news')
yc_webpage = res.text
soup = BeautifulSoup(yc_webpage, "html.parser")
article_texts=[]
article_links=[]
articles=soup.find_all(name="a", class_="titlelink")
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))
article_upvotes=[int(score.getText().replace(' points', '')) for score in soup.find_all(name="span", class_="score")]
highest_upvote = article_upvotes.index(max(article_upvotes))
highest_upvote_value = article_upvotes[highest_upvote]
print(article_texts[highest_upvote])
print(article_links[highest_upvote])
print(highest_upvote_value)


