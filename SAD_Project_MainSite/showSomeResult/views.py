from random import randint

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import Http404

from .forms import NameForm

from .models import TopGenre, motarjem
from .models import TranslationRequest,Language, BookMaker, Notification


def guide(request):
    return HttpResponse("use like this:<br>"
                        "http://127.0.0.1:8000/searchSTH/topGenre/"
                        "<br>OR<br>")


def show_top_genre(request):
    top_genre_list = TopGenre.objects.all()
    output = ', '.join([q.name for q in top_genre_list])
    return HttpResponse(output)


#     TODO hamid bas request.getbody bezane, vase inke betoone ba in adad ha kar kone
def getting_new_buy_request(request, buyedItems):
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


def bootiTest(request):
    return render(request, 'showSomeResult/bootStrapTest.html')


# THIS IS SEARCH PART
def search(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            req_id = form.cleaned_data["request_ID"]
            name = form.cleaned_data["book_name"]
            langs = form.cleaned_data.get('language')
            answer = list()
            for x in langs:
                # TODO in khat vaqean nabaiad bashe, model ha ie iradi darand ke majboor shodam in kar ro konam
                # bejaie khate paiin baiad az khode 'x' use mishod, masalan:
                #           temp = TranslationRequest.objects.filter(source_lang=x, BookName=name)
                langID = Language.objects.filter(language_name=x).values('id')[0]['id']

                if name != "":
                    if req_id != "":
                        temp = TranslationRequest.objects.filter(source_lang=langID, BookName=name, translation_request_id=req_id)
                    else:
                        temp = TranslationRequest.objects.filter(source_lang=langID, BookName=name)
                else:
                    if req_id != "":
                        temp = TranslationRequest.objects.filter(source_lang=langID, translation_request_id=req_id)
                    else:
                        temp = TranslationRequest.objects.filter(source_lang=langID)

                for i in range(len(temp)):
                    test = {'bookName': temp[i], 'reqID': temp[i].translation_request_id}
                    answer.append(test)

            return render(request, 'showSomeResult/SearchPageOfTarjomeList.html', {'bookList': answer})
    else:
        form = NameForm()

    return render(request, 'showSomeResult/SearchPageOfTarjomeList.html', {'form': form})


# THIS IS NOTIF TEST PAGE
def notif(request):
    return render(request, 'showSomeResult/NotifTemplate.html')


# THIS IS FOR RESPONSE TO NOTIF REQUESTS
def response_to_notifications_requests_by_js(request, user_id):
    user = BookMaker.objects.get(book_maker_id=user_id)
    # elate vojiide khate bala ine ke check konim useri ba moshakhaste bala tooie DB hast ia na ...
    notifications = list(Notification.objects.filter(BookMaker_id=user.book_maker_id))
    posts_serialized = serializers.serialize('json', notifications)
    return JsonResponse(posts_serialized, safe=False)


# vazifeie piade sazi e in ghesmat ba hamid hast
def hamidpart(request,motarjemID,requestID):
    user = BookMaker.objects.get(book_maker_id=motarjemID).__str__()
    book_name = TranslationRequest.objects.get(translation_request_id=requestID).__str__()
    return HttpResponse("I connect ("+user+") to translation of ("+book_name+") ")


def delete_notification(request, userID, notifPK):
    # vase in ino gozashtim ke aval check beshe ke aia intour user ii darim ia na
    user_obj = BookMaker.objects.get(book_maker_id=userID)
    notification_obj = Notification.objects.get(pk=notifPK)
    if notification_obj.BookMaker_id.book_maker_id == user_obj.book_maker_id:
        # TODO hala inja baiad in notif ro az DB pak konim
        return HttpResponse("done")

    return HttpResponse("Wrong")


# TODO baiad saiere user ha ro ham handle koni
def get_births_of_users(request, secretKey):
    if secretKey == "justShowMeTheBirthDay":
        answer = list()
        all_users = BookMaker.objects.all().values('name', 'last_name', 'birth_date')
        for x in all_users:
            answer.append(x)
        return JsonResponse(answer, safe=False)

    raise Http404("Don't try to do bad things ;)")