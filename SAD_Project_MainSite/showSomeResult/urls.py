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

    url(r'^bootiTest/$', views.bootiTest, name='bootiTest'),  # http://127.0.0.1:8000/searchSTH/bootiTest/
    url(r'^search/$', views.search, name='search'),  # http://127.0.0.1:8000/searchSTH/search/
    url(r'^notif/$', views.notif, name='notif'),  # http://127.0.0.1:8000/searchSTH/notif/

    # http://127.0.0.1:8000/searchSTH/showAllNotif/2/
    url(r'^showAllNotif/(?P<userID>[0-9]+)/$', views.responseToNotifJava, name='responseToNotifJava'),

    # http://127.0.0.1:8000/searchSTH/sendRequestAcceptanceToHamid/1/1
    url(r'^sendRequestAcceptanceToHamid/(?P<motarjemID>[0-9]+)/(?P<requestID>[0-9]+)/$',views.hamidpart, name='hamidpart'),

    # http://127.0.0.1:8000/searchSTH/deleteNotif/1/1
    url(r'^deleteNotif/(?P<userID>[0-9]+)/(?P<notifPK>[0-9]+)/$', views.deleteNotif,name='deleteNotif'),

    # http://127.0.0.1:8000/searchSTH/getBirthsOfUsers/justShowMeTheBirthDay
    # http://127.0.0.1:8000/searchSTH/getBirthsOfUsers/STHelse
    url(r'^getBirthsOfUsers/(?P<secretKey>[\w\-]+)/$', views.getBirthsOfUsers),
]