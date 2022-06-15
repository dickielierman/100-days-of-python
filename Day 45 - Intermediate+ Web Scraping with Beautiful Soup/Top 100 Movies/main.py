from bs4 import BeautifulSoup
import requests as req
res = req.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
yc_webpage = res.text
soup = BeautifulSoup(yc_webpage, "html.parser")
list_of_movies=[movie.getText() for movie in soup.select(selector="h3.title")]
list_of_movies.reverse()
with open('movie-to-watch.txt','w') as file:
    file.write('\n'.join(list_of_movies))
