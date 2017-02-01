import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, render_to_response
from itertools import chain
from django.views.generic.edit import CreateView
from .models import BookReaderUser, BookMaker, BookSeller, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import six, timezone
from django.http import *

# TODO need to check user's authority in all methods
@csrf_exempt
def book_reader_signup(request):
    if request.method == "GET":
        return render(request, 'bookreadersignup.html')
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        d_user = User.objects.create(username=jso['username'] , password=jso['password'] ,
                                     first_name=jso['first_name'] ,last_name=jso['last_name'] , email=jso['email'])
        user = BookReaderUser.objects.create(django_user=d_user,address=jso['address'], telephone_no=jso['tel_no'],
                                             birth_date_day=jso['day'], birth_date_month=jso['month'],
                                             birth_date_year=jso['year'])
        user.save()
        return redirect("/admin")


@csrf_exempt
def book_maker_signup(request):
    if request.method == "GET":
        return render(request, 'bookmakersignup.html')
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        d_user = User.objects.create(username=jso['username'], password=jso['password'], first_name=jso['first_name'],
                                     last_name=jso['last_name'], email=jso['email'])
        user = BookMaker.objects.create(django_user=d_user, birth_date=jso['birth_date'],
                                        telephone_no=jso['tel_no'],address=jso['address'],
                                        book_maker_type=jso['book_maker_type'], gender=jso['gender'])
        user.save()
        return redirect("/admin")


@csrf_exempt
def book_seller_signup(request):
    if request.method == "GET":
        return render(request, 'booksellersignup.html')
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        d_user = User.objects.create(username=jso['username'], password=jso['password'], first_name=jso['first_name'],
                                     last_name=jso['last_name'], email=jso['email'])
        user = BookSeller.objects.create(django_user=d_user, telephone_no=jso['tel_no'],
                                        address=jso['address'])
        user.save()
        return redirect("/admin")


# this method verify a book maker user
# caller must be an admin user, will be checked here
# request must contain the whole book maker user as a json
@csrf_exempt
def verify_book_maker_user(request):
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        # id is the primary key that must be in the json object
        p_key = jso['id']
        try:
            user = BookMaker.objects.get(pk=p_key)
            if not user.is_verified:
                user.is_verified = True
                user.save()
            else:
                print("User Already Verified!")
        except ObjectDoesNotExist:
            print("requested user does not exists!")


# works exactly like verify_book_maker_user
@csrf_exempt
def verify_book_seller_user(request):
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        # id is the primary key that must be in the json object
        p_key = jso['id']
        try:
            user = BookSeller.objects.get(pk=p_key)
            if not user.is_verified:
                user.is_verified = True
                user.save()
            else:
                print("User Already Verified!")
        except ObjectDoesNotExist:
            print("requested user does not exists!")


# use this method to show admin, a list of unverified bookmaker and bookseller
@csrf_exempt
def get_unverified_users(request):
    if request.method == "GET":
        unverified_book_makers = BookMaker.objects.filter(is_verified=False)
        unverified_book_sellers = BookSeller.objects.filter(is_verified=False)
        unverified_users = chain(unverified_book_sellers, unverified_book_makers)
        for element in unverified_users:
            print(element)
        return unverified_users
    # verifying bookseller and book maker
    # show list of unverified booksellers and bookmakers to the admin
    # give the option to verify users


# use this method to show admin, a list of undelivered orders
@csrf_exempt
def get_undelivered_orders(request):
    if request.method == "GET":
        unverified_orders = Order.objects.filter(delivery_date=None)
        output = {
            'unverified_orders': unverified_orders,
            'unverified_orders_count': unverified_orders.count(),
        }

        for element in unverified_orders:
            print(element)
        return unverified_orders


# use this method to set the delivery date of an order, thus verify that order is delivered
@csrf_exempt
def deliver_order(request):
    if request.method == "POST":
        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        # id is the primary key that must be in the json object
        p_key = jso['id']
        try:
            order = Order.objects.get(pk=p_key)
            if order.delivery_date is None:
                order.delivery_date = timezone.now()
            else:
                print("Order Already Delivered!")
        except ObjectDoesNotExist:
            print("requested Order Does not Exists!")


@csrf_exempt
def admin_page(request):
    output = {
        'unverified_book_makers' : BookMaker.objects.filter(is_verified=False),
        'unverified_book_makers_count': BookMaker.objects.filter(is_verified=False).count(),
        'unverified_book_sellers' : BookSeller.objects.filter(is_verified=False),
        'unverified_book_sellers_count' : BookSeller.objects.filter(is_verified=False).count()
    }

    print(output['unverified_book_makers'])
    print(output['unverified_book_makers_count'])
    print(output['unverified_book_sellers'])
    print(output['unverified_book_sellers_count'])
    return render_to_response('admin_page.html', output)


def logout_user(request):
    logout(request)
    return redirect("/")


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # this should redirect user to his homepage, based on the type of user he is
                return redirect("/")
            else:
                return render(request, 'user_not_active.html')

        else:
            return render(request, 'invalid.html')

    if request.method == "GET":
        return render(request, 'login.html')