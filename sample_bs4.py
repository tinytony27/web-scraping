from asyncore import write
import json
from work.robots import get_scraping_result
from work.utils import getHtmlBS4forUrl, writeCsv

json_data = []
wallkerplus_url = 'https://www.walkerplus.com/'

if not(get_scraping_result(wallkerplus_url)):
    print('Scrapingが許可されていないwebサイトです')
    exit()

# rangeで件数指定 9/25次点max=512
for i in range(1):
    index = i + 1
    url = wallkerplus_url + 'event_list/'+str(index)+'.html'
    soup = getHtmlBS4forUrl(url)

    json_docs = json.loads(soup.find('script').contents[0])

    for tmp in json_docs:
        json_tmp = {}
        # 要素を整理
        json_tmp['prefecture'] = tmp['location']['address']['addressRegion']
        json_tmp['eventName'] = tmp['name']
        json_tmp['eventArea'] = tmp['location']['address']['addressLocality']
        json_tmp['eventStartdate'] = tmp['startDate']
        json_tmp['eventEnddate'] = tmp['endDate']
        json_tmp['eventSpot'] = tmp['location']['name']
        json_tmp['telephone'] = tmp['telephone']
        json_tmp['description'] = tmp['description']
        json_tmp['url'] = tmp['url']
        json_tmp['type'] = tmp['@type']
        json_data.append(json_tmp)
        #json_data.append(tmp)
    
    print('get ' + str(index))

#print(len(json_data))
#print(json_data[0])

# csv出力
writeCsv(json_data, 'walkerplus.csv')

