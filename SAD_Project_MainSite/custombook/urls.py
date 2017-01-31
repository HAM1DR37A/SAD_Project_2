from django.conf.urls import url, include
from django.contrib import admin
from .views import register_translation_request

urlpatterns = [
    url(r'^trans_req/', register_translation_request),
]