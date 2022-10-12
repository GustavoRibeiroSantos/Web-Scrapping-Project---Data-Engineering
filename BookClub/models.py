import time
from django.db import models
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import psycopg2

# Create your models here.
class Model:
    def web_scraper():
        web_driver_started = Model.start_selenium()
        if web_driver_started is NameError:
            books_collected = Model.getInformation(web_driver_started)
            if books_collected:
                for book in books_collected:
                    Model.insert_book(book)
            else:
                print("list of books is empty!")
        else:
            print("WebDriver Error: ",NameError)

    def start_selenium ():
        try:
            options = Options()
            options.add_argument("--headless")
            WebBrowser = WebDriver(
            "C:/Users/Mars/OneDrive - Mars Inc/Área de Trabalho/first_project_data_engineering/static/Dependencies/chromedriver_win32/chromedriver.exe",
            options=options)
            return WebBrowser
        except NameError:
            return NameError

    def getInformation(WebBrowser):
        
        books_collected = []

        WebBrowser.get("http://books.toscrape.com/")
        if WebBrowser.request.response.status_code == 200:
            page_source = WebBrowser.page_source
            
            soup = BeautifulSoup(page_source, 'html.parser')
            tag = soup.find_all('ul', class_='nav nav-list')
            li = tag[0].find('li')
            ul = li.find('ul')
            caterories = ul.find_all('a', href=True)

            for caterory in range(0,len(caterories)):
                category_title = caterories[caterory].get_text()
                category_link = caterories[caterory]['href']

                WebBrowser.get(f"http://books.toscrape.com/{category_link}")
                time.sleep(5)
                page_source = WebBrowser.page_source

                soup = BeautifulSoup(page_source, 'html.parser')

                books = soup.find_all('article', class_='product_pod')
                        
                for book in books:
                    book_title = book.find('h3')
                    book_title = book_title.find('a')['title']
                    book_price = book.find('p',class_='price_color').get_text()
                    book_storage = book.find('p',class_='instock availability').get_text()
                    star_options = ["star-rating One","star-rating Two","star-rating Three","star-rating Four","star-rating Five"]
                    for star_amount in range(0,4):
                        if book.find('p',class_=star_options[star_amount]) != None:
                            break
                    
                    book = {
                        "Name": book_title,
                        "Category": category_title,
                        "Price": book_price,
                        "Storage": book_storage,
                        "Stars": star_amount
                    }
                    books_collected.append(book)

            return books_collected
        else:
            print("Page is not responding")

    def insert_book(book_props):
        try:
            conn = psycopg2.connect(
                    database="Books", user='postgres', password='admin', host='127.0.0.1', port= '5432'
                    )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(f'''CALL insert_data('{book_props["Name"].replace("'", "")}', '{book_props["Category"].strip()}','{book_props["Price"]}', '{book_props["Storage"].strip()}', '{book_props["Stars"] + 1}')''') 
        except NameError:
            return NameError
        else:
            return "Insert successfully."
        finally:
            # closing database connection.
            if conn:
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")

    def get_book_by_category(category):
        try:
            conn = psycopg2.connect(
                    database="Books", user='postgres', password='admin', host='127.0.0.1', port= '5432'
                    )
            conn.autocommit = True
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM BOOKS_TABLE Where category_book = '{category}'")
            books_selected = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
            return None
        else:
            return books_selected
        finally:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")





        