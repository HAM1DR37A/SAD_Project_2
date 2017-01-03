from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import TopGenre, BookForTarjome


def guide(request):
    return HttpResponse("use like this:<br>"
                        "http://127.0.0.1:8000/searchSTH/topGenre/<br>"
                        "OR<br>"
                        "http://127.0.0.1:8000/searchSTH/searchTarjome/1/")

def showTopGenre(request):
    top_genre_list = TopGenre.objects.all()
    output = ', '.join([q.name for q in top_genre_list])
    return HttpResponse(output)


def showTarjomeList(request,book_id):
    output = BookForTarjome.objects.get(id=book_id)
    return HttpResponse(output)