import requests
from bs4 import BeautifulSoup


response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

# Get the Titles
titles = soup.find_all(name="span", class_="titleline")
titles_text = [title.text for title in titles]

# Get the links related to the title
anchors = soup.select(".titleline a")
titles_anchor_raw_data = [a_tag.get("href") for a_tag in anchors if a_tag.get("href").startswith("https") or a_tag.get("href").startswith("item?")]

# Get the score of each title
subtexts = soup.find_all('td', class_='subtext')
scores = []

for subtext in subtexts:
    score_tag = subtext.find('span', class_='score')
    if score_tag:
        score_text = score_tag.getText()
        score = int(score_text.split()[0])
    else:
        score = 0

    scores.append(score)

highest_score = max(scores)
index_highest_score = scores.index(highest_score)

title_of_highest_score = titles_text[index_highest_score]
anchor_of_highest_score = titles_anchor_raw_data[index_highest_score]


print(highest_score)
print(title_of_highest_score)
print(anchor_of_highest_score)

