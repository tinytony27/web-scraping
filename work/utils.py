import requests
from bs4 import BeautifulSoup
import csv
import time


def getHtmlBS4forUrl(url):
    r = requests.get(url)
    # 相手のwebに迷惑（負荷）をかけないためのお作法
    time.sleep(2)
    return BeautifulSoup(r.content, 'html.parser')

def getHtmlBS4forHtml(html):
    return BeautifulSoup(html, 'html.parser')

# csv出力
def writeCsv(json_data, file_name):
    with open('./output/'+str(file_name), 'w', encoding='UTF-8', newline="") as f:
        csv.register_dialect('dialect01', doublequote=True, quoting=csv.QUOTE_ALL)
        writer = csv.DictWriter(f, fieldnames=json_data[0].keys(), dialect='dialect01')
        writer.writeheader()
        for target_dict in json_data:
            writer.writerow(target_dict)
        print('created csv file(' + str(file_name) + ').')