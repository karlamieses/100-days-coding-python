import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all(name="h3")
movies_titles_descending_order = [title.getText() for title in titles]
movies_titles_ascending_order = movies_titles_descending_order[::-1]

with open("movies.txt", mode="x") as file:
    for movie in movies_titles_ascending_order:
        file.write(f"{movie} \n")


