import os
from bs4 import BeautifulSoup

master = {}
file_name = "arizona.txt"


def scrape(html):
    # <tr class="odd views-row-first focus-within">
    soup = BeautifulSoup(html)
    table = soup.find_all("tr")

    # strip out the first and last rows as they don't contain any desired data
    table = table[1:-1]

    for row in table:
        key = str(row.a.contents[0].strip())
        val = row.span.contents[0].strip()

        if key == "Kaleidoscope SchoolÂ ÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂÂ":
            key = "Kaleidoscope School"

        data[key] = val

    return data


for x in range(19):
    url = "https://www.azed.gov/covid-19/learning-model-tracker?page=" + str(x)
    !curl
    {url} - o
    arizona.txt
    with open(file_name, "r") as file:
        html = file.read()
    master.update(scrape(html))

if os.path.exists(file_name):
    os.remove(file_name)
else:
    print("The file does not exist")