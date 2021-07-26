from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    try:
        all_category = Category.objects.all()
        all_article = Article.objects.all()
        context = {'categories': all_category, 'articles': all_article}
        return render(request, template_name=..., context=context)
    except Exception as ex:
        print(ex)
        return redirect(...)


def get_articles_by_category(request, id):
    try:
        articles = Article.objects.filter(category_id=id)
        return render(request, template_name=..., context={'articles': articles})
    except Exception as ex:
        print(ex)
        return redirect(...)


def get_all_users_articles(request, id):
    try:
        articles = Article.objects.filter(user_id=id)
        return render(request, template_name=..., context={'articles': articles})
    except Exception as ex:
        print(ex)
        return redirect(...)


def get_all_users_categories(request, id):
    try:
        categories = Category.objects.filter(parent_id=id)
        return render(request, template_name=..., context={'categories': categories})
    except Exception as ex:
        print(ex)
        return redirect(...)


def sing_up(request):
    """It`s view for registration User"""
    if request.method == 'POST':
        form = User_Sing_Up_Form(data=request.POST or None)
        if form.is_valid():
            form.save()
            user = form.get_user()
            login(request, user)
            messages.success(request, message='Congratulation you registered success!')
        else:
            messages.error(request, message='Registered error!')
    else:
        form = User_Sing_Up_Form()
    return render(request, template_name=..., context={'form': form})


def sing_in(request):
    """It`s view for login User"""
    if request.method == "POST":
        form = User_Sing_In_Form(data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Success you`re sing in!')
        else:
            messages.error(request, 'Sing In error!')
    else:
        form = User_Sing_In_Form()
    return render(request, template_name=..., context={'form': form})


def sing_out(request):
    """It`s view for logout User"""
    logout(request)
    messages.success('Success you`re sing out!')


def create_category(request):
    if request.method == 'POST':
        form = Category_Form(data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations you`re created category!')
        else:
            messages.error(request, 'Category creation error!')
    else:
        form = Category_Form()
    return render(request, template_name=..., context={'form': form})


def create_article(request):
    if request.method == 'POST':
        form = Article_Form(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations you`re created article!')
        else:
            messages.error(request, 'Article creation error!')
    else:
        form = Article_Form()
    return render(request, template_name=..., context={'form': form})
