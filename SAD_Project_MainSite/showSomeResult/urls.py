from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.guide, name='guide'),                                  # http://127.0.0.1:8000/searchSTH/
    url(r'^topGenre/$', views.showTopGenre, name='showTopGenre'),           # http://127.0.0.1:8000/searchSTH/topGenre/
    url(r'^tarjomeList/$', views.TarjomeList, name='TarjomeList'),  # http://127.0.0.1:8000/searchSTH/tarjomeList/
    # http://127.0.0.1:8000/searchSTH/takhfif/2/
    url(r'^takhfif/(?P<buyedItems>[0-9]+)/$', views.gettingNewBuyRequest, name='gettingNewBuyRequest'),
    # http://127.0.0.1:8000/searchSTH/update/2/
    url(r'^update/(?P<book_id>[0-9]+)/$', views.getNewTarjomeReq, name='getNewTarjomeReq'),
]