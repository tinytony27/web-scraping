import re
import urllib.robotparser

# 正規表現によりサイトのURLを取得
def get_root_url(url):
    pattern = r'(?P<root>https?://.*?)\/.*'
    result = re.match(pattern, url)
    if result is not None:
        root_url = result.group('root')
        print(f'ROOT URL -> {root_url}')
        return root_url
    print('Fail to get ROOT URL...')
    exit(1)

# サイトのURLからrobots.txtのURLを生成
def get_robots_txt_path(root_url):
    robots_txt_url = root_url + '/robots.txt'
    print(f'ROBOTS.TXT URL -> {robots_txt_url}')
    return robots_txt_url

def get_scraping_result(url):
    root_url = get_root_url(url)
    robots_txt_url = get_robots_txt_path(root_url)
    # robots.txtの読み取り
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_txt_url)
    rp.read()

    # robots.txtの情報から調査したいURL、User-Agentでクロール可能かを調べる
    user_agent = '*'
    result = rp.can_fetch(user_agent, root_url)
    print('Result: ' + str(result))
    return result

#url = 'https://www.walkerplus.com/*'
#get_robots_txt_path(get_root_url(url))
#get_scraping_result(url)