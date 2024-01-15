from bs4 import BeautifulSoup
import  requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
title = soup.find_all(class_="article-title-description__text")
movie_name = [name.find("h3").get_text() for name in title]
new_movie_name = reversed(movie_name)

# Specify the file path
file_path = 'movies.txt'

# Open the file in write mode and write each item to a new line
with open(file_path, 'w', encoding='utf-8') as file:
    for item in new_movie_name:
        file.write(f"{item}\n")
