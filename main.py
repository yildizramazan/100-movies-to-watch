import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"




response = requests.get(url=URL).text
soup = BeautifulSoup(response, "html.parser")
all_tags = soup.find_all(name="h3", class_="title")
all_titles = [tag.getText() for tag in all_tags][::-1]


with open(file="movies.txt", mode="w") as file:
    file.writelines([f"{line}\n" for line in all_titles])



print(all_titles)




