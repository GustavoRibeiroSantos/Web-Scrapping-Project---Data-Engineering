from unicodedata import category
from django.shortcuts import render
from .models import Model
import csv

def end_point_web_scraper(request):
    Model.web_scraper()   

def end_point_get_books_by_category(request, category):
    books_selected = Model.get_book_by_category(category)
    return books_selected

def end_point_get_books_by_category_csv(request, category):
    books_selected = Model.get_book_by_category(category)
    book_header = ["ID_BOOK","NAME_BOOK","STORAGE_BOOK","N_STAR_BOOK","CATEGORY_BOOK","PRICE_BOOK"]
    with open(f'C:/Users/Mars/OneDrive - Mars Inc/{category}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(book_header)
        # Use writerows() not writerow()
        for book in books_selected:
            print(book)
        writer.writerows(books_selected)
        print("File created...")