from django.urls import path
from .views import end_point_get_books_by_category, end_point_get_books_by_category_csv, end_point_web_scraper

urlpatterns = [
    path('',end_point_web_scraper),
    path('get_book/<str:category>', end_point_get_books_by_category, name='index'),
    path('get_book_csv/<str:category>', end_point_get_books_by_category_csv, name='index'),
]