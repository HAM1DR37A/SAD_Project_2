import json
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import CreateView
from authsystem.models import BookReaderUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils import six
from django.http import *


@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, 'bookreadersignup.html')
    if request.method == "POST":
        print(request.POST)

        post_dict = dict(six.iterlists(request.POST))
        jso = json.loads(post_dict['command'][0])
        print(jso['first_name'])

        # if(jso['password'] == jso['r_password']):
        #     return JsonResponse({'status': 'ok'})
        # else:
        #     return JsonResponse({'status': 'siktir'})
        d_user = User.objects.create(username=jso['username'] , password=jso['password'] ,first_name=jso['first_name'] , last_name=jso['last_name'] , email=jso['email'])
        user = BookReaderUser.objects.create(django_user=d_user,address=jso['address'], telephone_no=jso['tel_no'])
        user.save()


def main(request):
    if request.method == "GET":
        return render(request, 'main.html')