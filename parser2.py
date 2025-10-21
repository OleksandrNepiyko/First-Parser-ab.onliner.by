from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date

review_parameters = {
    "rate": "5",
    "parse_date": "2025-12-31",
    "description": "description",
    "author_name": "name",
    "review_date": "2025-12-31",
    "photo": "photo",
    "brand": "brand",
    "model": "model",   
    "year": "2024",
    "body_type": "седан",
    "engine": "2.0L",
    "transmission": "автомат",
    "drive_type": "передній",
    "fuel_type": "бензин",
    "html": "code",
    "link": "https://ab.onliner.by/reviews"
}


driver = webdriver.Chrome()
driver.get("https://ab.onliner.by/reviews")
driver.find_element(By.CLASS_NAME, "input-style__real").click()

brands = driver.find_elements(By.CLASS_NAME, "dropdown-style__checkbox-sign")
brands.pop(0)
brands_list = [brand.text for brand in brands]
for brand in brands_list:
    print( )
    print( )
    print(brand)
    link = f"https://ab.onliner.by/reviews/{brand.lower()}"
    brand_page = driver.get(link)
    # if brand_page:
    time.sleep(3)
    links_to_reviews = driver.find_elements(By.CLASS_NAME, "vehicle-form__offers-stub")
    review_links = [url.get_attribute('href') for url in links_to_reviews if url.get_attribute('href')]
    for review_url in review_links:
        if review_url:
            review_page = driver.get(review_url)
            time.sleep(3)
            rate = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div").text
            parse_date = date.today()
            description = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[5]/div/div/div[1]/div/div/div/p").text
            print(rate)
            print(parse_date)
            print(description)
            driver.back()
            time.sleep(2)

        # author_name =
        # review_date =
        # photo =
        # brand =
        # model =
        # year =
        # body_type =
        # engine =
        # transmission =
        # drive_type =
        # fuel_type =
        # html =
        # link =

# else:
#     print("brand page not found")

# save htmls only each review

driver.close()
driver.quit()
