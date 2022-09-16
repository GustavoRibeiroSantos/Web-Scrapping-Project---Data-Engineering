import time
from django.db import models
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Create your models here.
class Model:
    def start_selenium ():
        options = Options()
        options.add_argument("--headless")
        # options.add_argument('--window-size=1920,1080')
        # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        # options.add_argument(f"user-agent={user_agent}")

        browser = webdriver.Chrome(
        "C:/Users/Mars/OneDrive - Mars Inc/Área de Trabalho/first_project_data_engineering/static/Dependencies/chromedriver_win32/chromedriver.exe",
        options=options)

        return browser

    def getInformation(browser):

        browser.get("http://books.toscrape.com/")
        time.sleep(10)
        page_source = browser.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        tag = soup.find_all('ul', class_='nav nav-list')
        li = tag[0].find('li')
        ul = li.find('ul')
        a = ul.find_all('a', href=True)

        for i in range(0,len(a)):
            category = a[i].get_text()
            category_link = a[i]['href']

            browser.get(f"http://books.toscrape.com/{category_link}")
            time.sleep(10)
            page_source = browser.page_source

            soup = BeautifulSoup(page_source, 'html.parser')

            books = soup.find_all('article', class_='product_pod')
            print(f'Categoria selecionada: {category_link}')
            print(books)



        