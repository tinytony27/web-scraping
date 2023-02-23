from work.robots import get_scraping_result
from work.utils import getHtmlBS4forHtml

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

json_data = []
wallkerplus_url = 'https://mugendai.yoshimoto.co.jp/schedule/'

if not(get_scraping_result(wallkerplus_url)):
    print('Scrapingが許可されていないwebサイトです')
    exit()

options = Options()
# ヘッドレスモードで実行する場合
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

try:
	# 取得先URLにアクセス
	driver.get(wallkerplus_url)
	
	# コンテンツが描画されるまで待機
	time.sleep(5)

	# 対象を抽出
	values = driver.find_element(By.ID, "schedule2023-02-23")
	print(getHtmlBS4forHtml(values.get_attribute('innerHTML')))
finally:
	# プラウザを閉じる
	driver.quit()

