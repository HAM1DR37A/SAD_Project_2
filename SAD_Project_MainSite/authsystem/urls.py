from django.conf.urls import url, include
from django.contrib import admin
from .views import book_reader_signup, get_unverified_users, book_maker_signup, book_seller_signup, admin_page

urlpatterns = [
    url(r'^admin_page/', get_unverified_users),
    url(r'^book_reader_signup/', book_reader_signup),
    url(r'^book_maker_signup/', book_maker_signup),
    url(r'^book_seller_signup/', book_seller_signup),
    url(r'^admin_page/', admin_page),
]