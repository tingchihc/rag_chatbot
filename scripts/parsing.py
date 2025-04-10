import json
import os
import requests
from bs4 import BeautifulSoup

def parsing():
    url = "https://movies.fandom.com/wiki/Cars/Transcript"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data_dict = {}
    dl_tags = soup.find_all('dl')

    item_id = 1 
    for dl in dl_tags:
        dd_tags = dl.find_all('dd')
        for dd in dd_tags:
            bold_tag = dd.find('b')
            if bold_tag:
                b_text = bold_tag.get_text(strip=True)
                bold_tag.extract()
                info_text = dd.get_text(strip=True)
                data_dict[item_id] = {
                    'b': b_text,
                    'info': info_text
                }
                item_id += 1

    with open("data.json", 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=4)
    
    with open('info_output.txt', 'w', encoding='utf-8') as f:
        for item in data_dict.values():
            tmp = item["info"].replace(":", "", 1)
            f.write(tmp + '\n')


parsing()
