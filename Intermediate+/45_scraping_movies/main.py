import requests
from bs4 import BeautifulSoup

movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=movies_url)
content = response.text
soup = BeautifulSoup(content, "html.parser")

titles = soup.find_all(name="h3", class_="title")
# print(len(titles), titles[0])
titles = [title.getText() for title in titles[::-1]]
movies = "\n".join(titles)

with open("movies.txt", "w", encoding="utf-8") as file:
    file.write(movies)

