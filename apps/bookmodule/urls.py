from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="books.index"),
    path("list_books/", views.list_books, name="books.list_books"),
    path('html5/links/', views.links_view, name='books.html5_links'),
    path('html5/text/formatting/', views.text_formatting_view, name='books.html5_formatting'),
    path('lab9/task6', views.lab9_task6, name='lab9_task6'),
    path("<int:bookId>/", views.viewbook, name="books.view_one_book"),
    path("aboutus/", views.aboutus, name="books.aboutus"),
    
]