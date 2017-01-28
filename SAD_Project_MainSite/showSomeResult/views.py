from random import randint

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import TopGenre, BookForTarjome, motarjem


def guide(request):
    return HttpResponse("use like this:<br>"
                        "http://127.0.0.1:8000/searchSTH/topGenre/"
                        "<br>OR<br>"
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


def bootiTest(request):
    return render(request, 'showSomeResult/bootiTest.html')


# THIS IS SEARCH PART
from .forms import NameForm
from .models import TranslationRequest,Language
def search(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data["request_ID"]
            name = form.cleaned_data["book_name"]
            langs = form.cleaned_data.get('language')
            # TODO alan baiad be list e tarjome ie search bezanim bar asas e id va name, baadesh nataiej ro be safhe befrestim ta neshoon bede
            answer= list()
            for x in langs:
                # TODO in khat vaqean nabaiad bashe, model ha ie iradi darand ke majboor shodam in kar ro konand
                langID = Language.objects.filter(language_name=x).values('id')[0]['id']
                # TODO, bejaie khate bala baiad az khode 'x' usemishod, masalan:
                #           temp = TranslationRequest.objects.filter(source_lang=x, BookName=name)

                if name != "":
                    if id != "":
                        temp = TranslationRequest.objects.filter(source_lang=langID, BookName=name, translation_request_id=id)
                    else:
                        temp = TranslationRequest.objects.filter(source_lang=langID, BookName=name)
                else:
                    if id != "":
                        temp = TranslationRequest.objects.filter(source_lang=langID, translation_request_id=id)
                    else:
                        temp = TranslationRequest.objects.filter(source_lang=langID)



                for i in range(len(temp)):
                    answer.append(temp[i])

            return render(request,'showSomeResult/SearchPageOfTarjomeList.html',{'bookList':answer})
    else:
        form = NameForm()

    return render(request, 'showSomeResult/SearchPageOfTarjomeList.html',{'form': form})



# THIS IS NOTIF TEST PAGE
def notif(request):
    return render(request, 'showSomeResult/NotifTemplate.html')

# THIS IS FOR RESPONSE TO NOTIF REQUESTS
from .models import BookMaker, Notification
from django.http import JsonResponse
from django.core import serializers
def responseToNotifJava(request, userID):
    user = BookMaker.objects.get(book_maker_id=userID) #TODO in khat fln ke ezafii be nazar mirese, kolan model ha kheili irad darand :|
    notifs = list(Notification.objects.filter(BookMaker_id=user.book_maker_id))
    posts_serialized = serializers.serialize('json', notifs)
    return JsonResponse(posts_serialized, safe=False)
