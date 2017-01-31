import json
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import CreateView
from .models import BookReaderUser, BookMaker
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import six
from django.http import *

def signup_some_book_maker():
    d_user = User.objects.create(username=input("enter username: "), password=input("enter password: "),
                                 first_name=input("enter first_name: "),
                                 last_name=input("enter last Name: "), email=input("Enter Email: "))
    user = BookMaker.objects.create(django_user=d_user, birth_date="1994-04-04", telephone_no="0090",
                                    address="Cemetery", book_maker_type=input("Enter Type: "),
                                    gender=input("Enter Gender: "))
    user.save()


def verify_test(request):
    if request.method == "GET":
        verify_book_maker_test()
@csrf_exempt
def book_reader_signup(request):
    if request.method == "GET":
        signup_some_book_maker()
        return render(request, 'bookreadersignup.html')
    if request.method == "POST":
        print(request.POST)

        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        print(jso['first_name'])
        d_user = User.objects.create(username=jso['username'] , password=jso['password'] ,first_name=jso['first_name'] ,last_name=jso['last_name'] , email=jso['email'])
        user = BookReaderUser.objects.create(django_user=d_user,address=jso['address'], telephone_no=jso['tel_no'])
        user.save()


@csrf_exempt
def book_maker_signup(request):
    if request.method == "GET":
        return render(request, 'bookmakersignup.html')
    if request.method == "POST":
        print(request.POST)

    post_dict = dict(six.iterlists(request.POST))
    jso = json.loads(post_dict['command'][0])
    d_user = User.objects.create(username=jso['username'], password=jso['password'], first_name=jso['first_name'],
                                 last_name=jso['last_name'], email=jso['email'])
    user = BookMaker.objects.create(django_user=d_user, birth_date=jso['birth_date'], telephone_no=jso['tel_no'],address=jso['address'], book_maker_type=jso['book_maker_type'], gender=jso['gender'])
    user.save()


@csrf_exempt
def book_seller(request):
    if request.method == "GET":
        return render(request, 'booksellersignup.html')
    if request.method == "POST":
        print(request.POST)

    post_dict = dict(six.iterlists(request.POST))
    jso = json.loads(post_dict['command'][0])
    d_user = User.objects.create(username=jso['username'], password=jso['password'], first_name=jso['first_name'],
                                 last_name=jso['last_name'], email=jso['email'])
    user = BookMaker.objects.create(django_user=d_user, telephone_no=jso['tel_no'],
                                    address=jso['address'])
    user.save()


# this method verify a book maker user
# caller must be an admin user, will be checked here
# request must contain the whole book maker user as a json
@csrf_exempt
def verify_book_maker_user(request):
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        # book_maker_id is the primary key that must be in the json object
        p_key = jso['id']
        user = BookMaker.objects.get(pk=p_key)
        if user.is_verified == False:
            user.is_verified = True
            user.save()
            print(user.is_verified)
        else:
            print("User Already Verified!")


def verify_book_maker_test():
    p_key = '1'
    user = BookMaker.objects.get(id=p_key)
    if user.is_verified == False:
        user.is_verified = True
        user.save()
        print(user.is_verified)
    else:
        print("User Already Verified!")
@csrf_exempt
def get_unverified_users(request):
    if request.method == "GET":
        unverified_users = BookMaker.objects.filter(is_verified=False)
        print(unverified_users)
        return render(request, 'bookreadersignup.html')
    # verifying bookseller and book maker
    # show list of unverified booksellers and bookmakers to the admin
    # give the option to verify users
    #