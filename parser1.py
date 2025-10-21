from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

url = 'https://ab.onliner.by/reviews/bmw/5-seriya/e34'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text


# print(src)

soup = BeautifulSoup(src, "lxml")

vehicles_list = soup.find("div", class_="vehicle-form__description vehicle-form__description_base vehicle-form__description_primary vehicle-form__description_condensed-complementary")
# var = soup.find("a", class_="vehicle-form__offers-stub")
# print(vehicles_list[1])
# for i in vehicles_list:
#     print (i.text)
# print (var)
print (vehicles_list)

var = soup.find("nav", "b-top-navigation")
print(var)

# soup = BeautifulSoup()

