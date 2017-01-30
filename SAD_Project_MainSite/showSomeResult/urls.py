from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.guide, name='guide'),                                  # http://127.0.0.1:8000/searchSTH/
    url(r'^topGenre/$', views.show_top_genre, name='show_top_genre'),       # http://127.0.0.1:8000/searchSTH/topGenre/

    # http://127.0.0.1:8000/searchSTH/takhfif/2/
    url(r'^takhfif/(?P<buyedItems>[0-9]+)/$', views.getting_new_buy_request, name='getting_new_buy_request'),

    url(r'^bootiTest/$', views.bootiTest, name='bootiTest'),  # http://127.0.0.1:8000/searchSTH/bootiTest/
    url(r'^search/$', views.search, name='search'),  # http://127.0.0.1:8000/searchSTH/search/
    url(r'^notif/$', views.notif, name='notif'),  # http://127.0.0.1:8000/searchSTH/notif/

    # http://127.0.0.1:8000/searchSTH/showAllNotif/2/
    url(r'^showAllNotif/(?P<userID>[0-9]+)/$', views.response_to_notif_java, name='response_to_notif_java'),

    # http://127.0.0.1:8000/searchSTH/sendRequestAcceptanceToHamid/1/1
    url(r'^sendRequestAcceptanceToHamid/(?P<motarjemID>[0-9]+)/(?P<requestID>[0-9]+)/$',views.hamidpart, name='hamidpart'),

    # http://127.0.0.1:8000/searchSTH/deleteNotif/1/1
    url(r'^delete_notification/(?P<userID>[0-9]+)/(?P<notifPK>[0-9]+)/$', views.delete_notification, name='delete_notification'),

    # http://127.0.0.1:8000/searchSTH/getBirthsOfUsers/justShowMeTheBirthDay
    # http://127.0.0.1:8000/searchSTH/getBirthsOfUsers/STHelse
    url(r'^get_births_of_users/(?P<secretKey>[\w\-]+)/$', views.get_births_of_users),
]