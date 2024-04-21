from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://scraping-for-beginner.herokuapp.com/udemy"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
#print(soup.prettify())

soup.find_all("p")

# options = Options()
# options.add_argument("--headless")

# ブラウザを起動してURLにアクセスする
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://scraping-for-beginner.herokuapp.com/login_page")

# 要素（場所）を指定して、そこに対して文字を入力
elem_username = browser.find_element_by_id("username")
elem_username.send_keys("imanishi")

elem_password = browser.find_element_by_id("password")
elem_password.send_keys("kohei")

# 要素（場所）を指定して、ボタンをクリック
sleep(1)
elem_login_btn = browser.find_element_by_id("login-btn")
elem_login_btn.click()

WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, "th"))
)

elems_th = browser.find_elements(By.TAG_NAME, "th")
keys = []
for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

elems_td = browser.find_elements(By.TAG_NAME, "td")
values = []
for elem_td in elems_td:
    value = elem_td.text
    values.append(value)

df = pd.DataFrame()
df["項目"] = keys
df["値"] = values

df.to_csv("講師情報.csv", index=False)

elem = browser.find_element_by_id("name")
name = elem.text
print(name)

elem = browser.find_element_by_id("company")
company = elem.text
print(company)

elem = browser.find_element_by_id("birthday")
birthday = elem.text
print(birthday)

elem = browser.find_element_by_id("come_from")
come_from = elem.text
print(come_from)

elem = browser.find_element_by_id("hobby")
hobby = elem.text
print(hobby.replace("\n", ","))

elem_th = browser.find_element_by_tag_name("th")
elem_th.text

elems_th = browser.find_elements_by_tag_name("th")
elems_th.text
print(len(elems_th))

browser.quit()