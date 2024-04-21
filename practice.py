from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import requests

# ブラウザを起動してURLにアクセスする
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.moguravr.com/category/metaverse-news/")

data = []

try:
    # main main タグ内の最初の a タグを待機してから取得
    links = WebDriverWait(browser, 10).until(
        EC.visibility_of_all_elements_located((By.TAG_NAME, "main main a"))
    )
    for link in links:
        datum = {}

        sleep(1)
        link.click()
        url = browser.page_source
        soup = BeautifulSoup(url, 'html.parser')

        title = soup.find('h1').text

        date = soup.find_all("span", attrs={"class": "text-muted small ml-1"})[0]
        date = date.text.replace("\n", "")

        datum["title"] = title
        datum["date"] = date
        print(datum)

        data.append(datum)
        break
        browser.back()

except Exception as e:
    print(f"An error occurred: {e}")