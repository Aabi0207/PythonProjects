from bs4 import BeautifulSoup
import html

with open("source_code.txt", encoding="UTF-8") as data:
    source_code = data.read()

soup = BeautifulSoup(source_code, "html.parser")

all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")
top_100_movies = [movie.get_text().replace("\xa0", "") for movie in all_movies]
print(top_100_movies)

with open("top_100_movies.txt", "w") as data:
    for movie in top_100_movies:
        data.write(movie + "\n")