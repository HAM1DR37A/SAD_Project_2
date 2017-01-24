from django.shortcuts import render, redirect, render_to_response
from django.views.generic.edit import CreateView
from authsystem.models import BookReaderUser
#from content.models import UserGroupAssignment, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as AuthUser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class BookReaderSignUp(CreateView):
    model = BookReaderUser
    fields = ['username', 'password', 'telephone_no', 'address', 'avatar']

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']

        djuser = AuthUser.objects.create(username = username, password = password)

        bookreaderuser = BookReaderUser.objects.create(django_user= djuser)

        user = form.save(commit=True)
        # user.set_password(password)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, user)
        return super(BookReaderUser, self).form_valid(form)

#
# class MyUserCreate(CreateView):
#
#     model = RegisteredUser
#     fields = ['displayName', 'gender', 'avatar']
#     success_url = "/main"
#
#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.user = self.request.user
#         user.id = self.request.user.id
#         print(self.request.user)
#         return super(MyUserCreate, self).form_valid(form)
#
#     # success_url = url
#
#
# def logout_user(request):
#     logout(request)
#     return redirect("/")
#
# @csrf_exempt
# def login_user(request):
#     if (request.method == 'POST'):
#         username = request.POST.get('username')
#         print(username)
#         password = request.POST.get('password')
#         print(password)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 usergroupass = UserGroupAssignment.objects.filter(userId__user=request.user).first().groupId.id
#                 return redirect("/main/{0}".format(Group.objects.filter(id=usergroupass).first().id))
#             else:
#                 return render(request, 'user_not_active.html')
#
#         else:
#
#             return render(request, 'invalid.html')
#     else:
#         return render(request, 'login.html')
#
#


