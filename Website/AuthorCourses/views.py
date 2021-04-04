# Create your views here.
import email

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.views.generic import DetailView

from .forms import SignUpForm, DocumentForm, ContentForm
from .models import AllContents


# @login_required(login_url='AuthorCourses:login')
def home_view(request):
    return render(request, 'AuthorCourses/home.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('AuthorCourses:home')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('AuthorCourses:login')

        context = {'form': form}
        return render(request, 'AuthorCourses/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('AuthorCourses:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=username, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('AuthorCourses:home')
            else:
                messages.success(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'AuthorCourses/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('AuthorCourses:login')


# @login_required(login_url='AuthorCourses:login')
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('AuthorCourses:home')
    else:
        form = DocumentForm()
    return render(request, 'AuthorCourses/model_form_upload.html', {
        'form': form
    })


# @login_required(login_url='AuthorCourses:login')
def item_list(request):
    context = {'item_list': AllContents.objects.all()}
    return render(request, "AuthorCourses/item_list.html", context)


# @login_required(login_url='AuthorCourses:login')
def item_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ContentForm(entry=())
        else:
            item = AllContents.objects.get(pk=id)
            form = ContentForm(instance=item, entry=item)
        return render(request, "AuthorCourses/item_form.html", {'form': form})
    else:
        if id == 0:
            form = ContentForm(request.POST, entry=())
        else:
            item = AllContents.objects.get(pk=id)
            form = ContentForm(request.POST, instance=item, entry=item)
        if form.is_valid():
            form.save()
        return redirect('/list')


# @login_required(login_url='AuthorCourses:login')
def item_delete(request, id):
    item = AllContents.objects.get(pk=id)
    item.delete()
    return redirect('/list')


# @login_required(login_url='AuthorCourses:login')
def show_content(request, content_id):
    content = AllContents.objects.get(pk=content_id)
    return render(request, 'AuthorCourses/show_content.html',
                  {'content': content})


# @login_required(login_url='AuthorCourses:login')
def search_contents(request):
    if request.method == "POST":
        searched = request.POST['searched']
        contents = AllContents.objects.filter(Q(contentName__contains=searched) | Q(contentBody__contains=searched) | Q(
            contentSummary__contains=searched) | Q(category__name__contains=searched))

        return render(request,
                      'AuthorCourses/search_contents.html',
                      {'searched': searched,
                       'contents': contents})
    else:
        return render(request,
                      'AuthorCourses/search_contents.html',
                      {})


# class ContentDetail(DetailView):
#     model = AllContents
