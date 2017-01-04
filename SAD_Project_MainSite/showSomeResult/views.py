from random import randint

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import TopGenre, BookForTarjome, motarjem


def guide(request):
    return HttpResponse("use like this:<br>"
                        "http://127.0.0.1:8000/searchSTH/topGenre/<br>"
                        "OR<br>"
                        "http://127.0.0.1:8000/searchSTH/tarjomeList/")


def showTopGenre(request):
    top_genre_list = TopGenre.objects.all()
    output = ', '.join([q.name for q in top_genre_list])
    return HttpResponse(output)


def TarjomeList(request):
    list = BookForTarjome.objects.all()
    output = ', '.join([q.name for q in list])
    return HttpResponse(output)


#     TODO hamid bas request.getbody bezane, vase inke betoone ba in adad ha kar kone
def gettingNewBuyRequest(request, buyedItems):
    # age taraf iedoone kharid kone, shansesh ro ba adad e 13 check mikonim :)) age biare %10 migire
    buyedItems = int(buyedItems)
    if buyedItems == 1:
        return HttpResponse('10') if randint(0, 1000) == 13 else HttpResponse('0')
    if 1 < buyedItems < 5:
        return HttpResponse('5')
    if 5 <= buyedItems < 10:
        return HttpResponse('7')
    if 10 <= buyedItems:
        return HttpResponse('10')


def getNewTarjomeReq(request, book_id):
    bookName = BookForTarjome.objects.get(id=book_id).__str__()
    booklang = BookForTarjome.objects.get(id=book_id).lang
    motarjems = motarjem.objects.filter(desiredLang=booklang)
    for x in motarjems:
        x.notification = "got this for you to translate ==> "+str(bookName)+"  go to search tab and " \
                                                                            "search for this id:"+str(book_id)
        x.save()
    output = '<br> '.join(["user:"+q.name+"||notif:"+q.notification for q in motarjems])
    return HttpResponse(output)
