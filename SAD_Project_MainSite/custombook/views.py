import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, render_to_response
from itertools import chain
from django.views.generic.edit import CreateView
from SAD_Project_MainSite.authsystem.models import TranslationRequest, BookReaderUser, BookMaker, PreOrder, Book,Write
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import six, timezone
from django.http import *


# TODO need to check user's authority in all methods
@csrf_exempt
def register_translation_request(request):
    if request.method == "GET":
        # structure of form defined below
        return render(request, 'registertranslationrequest.html')
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        if request.user.is_authenticated:
            user = BookReaderUser.objects.filter(django_user=request.user)
        else:
            print("Anonymous User Error!")
        if len(user) < 1:
            print("Invalid User!")
        else:
            t_req = TranslationRequest.objects.create(dbook_file=jso['book_file'],
                                                  book_name=jso['book_name'], source_lang=jso['source_lang'],
                                                  user_id=user, register_date=timezone.now())
            t_req.save()


# this method add a book to the pre-orderable books
@csrf_exempt
def register_a_book_for_pre_order(request):
    if request.method == "GET":
        # structure of form defined below
        return render(request, 'addbookforpreorder.html')
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        if request.user.is_authenticated:
            user = BookMaker.objects.filter(django_user=request.user)
        else:
            print("Anonymous User Error!")
        if len(user) < 1:
            print("Invalid User!")
        else:
            book = Book.objects.create(title=jso['title'], first_publish_year=int(jso['publish_year']), isbn=jso['isbn'],
                                       number_of_pages=int(jso['number_of_pages']), summary=jso['summary'],
                                       cover_image_addr=jso['cover_image'], author_name=jso['author_name'])
            book.save()
            w_entry = Write.objects.create(book_id=book, book_maker_id=user)
            w_entry.save()


# TODO this method should be called after receiving bank's verification
@csrf_exempt
def pre_order_a_book(request):
    if request.method == "GET":
        return render(request, 'preorderabook.html')
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        if request.user.is_authenticated:
            user = BookReaderUser.objects.filter(django_user=request.user)
        else:
            print("Anonymous User Error!")
        if len(user) < 1:
            print("Invalid User!")
        else:
            pre_order = PreOrder.objects.create(user_name=user, book_id=jso['book_id'], quantity=int(jso['quantity']))
            pre_order.save()