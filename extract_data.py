from bs4 import BeautifulSoup
import requests
import re


def extract_from_web(file_name):
    # specify url
    url = 'http://www.koeri.boun.edu.tr/scripts/lst0.asp'

    # request html
    page = requests.get(url)

    # Parse html using BeautifulSoup, you can use a different parser like lxml
    soup = BeautifulSoup(page.content, "html.parser")

    # find searches the given tag (div) with given class attribute and returns the first match it finds
    all_text = soup.find('pre')

    # Extracting the text out of the div
    data_txt = open(file_name, "w", encoding="utf-8")
    data_txt.write(all_text.text)


def clean_data_extracted(file_name):
    with open(file_name, "r+", encoding="utf-8") as fl:
        all_text = fl.read()

        # extract only earthquake data
        regex = re.compile("--------------\n(.*)\n{2}", re.MULTILINE | re.DOTALL)

        # to get the cleaned text
        text_cleaned = re.search(regex, all_text).group(1)

        regex_location = re.compile(r"([a-zA-Z])(\s)([a-zA-Z()])")
        text_cleaned = re.sub(regex_location, r"\1-\3", text_cleaned)

        fl.seek(0)
        fl.write(text_cleaned)
        fl.truncate()


def create_dict(file_name):
    all_data = list()
    for line in open(file_name, "r", encoding="utf-8"):
        split_data = line.split()

        # our data
        date = split_data[0]
        time = split_data[1]
        latitude = split_data[2]
        longitude = split_data[3]
        depth = split_data[4]
        magnitude = split_data[6]
        location = split_data[8]

        data = {
            "date": date,
            "time": time,
            "latitude": latitude,
            "longitude": longitude,
            "depth": depth,
            "magnitude": magnitude,
            "location": location
        }

        all_data.append(data)

    return all_data

