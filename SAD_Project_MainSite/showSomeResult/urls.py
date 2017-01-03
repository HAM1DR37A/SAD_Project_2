from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.guide, name='guide'),
    url(r'^topGenre/$', views.showTopGenre, name='showTopGenre'),
    url(r'^searchTarjome/(?P<book_id>[0-9]+)/$', views.showTarjomeList, name='showTarjomeList'),        # ex: /polls/5/
]