from bs4 import BeautifulSoup
with open('website.html', encoding="utf8") as file:
    webpage = file.read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title)

all_a_tags = soup.find_all(name="a")
print(all_a_tags)

heading = soup.find(class_="heading")
print(heading.get_text())

the_one_link = soup.select_one(selector="p a")
