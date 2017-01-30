from django.conf.urls import url, include
from django.contrib import admin
from .views import book_reader_signup
# from SAD_Project_MainSite.authsystem.views import signup,main

urlpatterns = [
    # url(r'^searchSTH/', include('showSomeResult.urls')),
    url(r'^signup/', book_reader_signup),
  #  url(r'^signup/$', signup),
  #   url(r'^$', main)
]