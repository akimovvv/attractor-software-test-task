from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    """This view for main page. Here it get all categories and articles and send to templates"""
    try:
        all_category = Category.objects.all()
        all_article = Article.objects.all().order_by('updated_at')[::-1]
        context = {'categories': all_category, 'articles': all_article}
        return render(request, template_name='main/index.html', context=context)
    except Exception as ex:
        print(ex)
        return redirect('/')


def get_articles_by_category(request, category_id):
    """This view for little filter getting all articles from one category"""
    try:
        articles = Article.objects.filter(category_id=category_id).order_by('updated_at')[::-1]
        all_category = Category.objects.all()
        context = dict(articles=articles, categories=all_category)
        return render(request, template_name='main/list_category_view.html', context=context)
    except Exception as ex:
        print(ex)
        return redirect('/')


def get_all_user_data(request):
    """This view for user profile. Here i get all user created articles to give chance to delete or edit"""
    try:
        articles = Article.objects.filter(user_id=request.user.id).order_by('updated_at')[::-1]
        categories = Category.objects.all()
        context = {'articles': articles, 'categories': categories}
        return render(request, template_name='main/my_profile.html', context=context)
    except Exception as ex:
        print(ex)
        return redirect('/')


def sing_up(request):
    """It`s view for registration User"""
    if request.method == 'POST':
        form = User_Sing_Up_Form(data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, message='Congratulation you registered success!')
            return redirect(to='sing_in')
        else:
            messages.error(request, message='Registered error!')
    else:
        form = User_Sing_Up_Form()
    return render(request, template_name='main/sing-up.html', context={'form': form})


def sing_in(request):
    """It`s view for login User"""
    if request.method == "POST":
        form = User_Sing_In_Form(data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Success you`re sing in!')
            return redirect('/')
        else:
            messages.error(request, 'Sing In error!')
    else:
        form = User_Sing_In_Form()
    return render(request, template_name='main/sing-in.html', context={'form': form})


def edit_user(request):
    """This view for edit user username or password"""
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.user.id)
            form = User_Sing_Up_Form(data=request.POST)
            if form.is_valid():
                user.username = form.cleaned_data.get('username')
                print(user.password, form.cleaned_data.get('password1'))
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                messages.success(request, "Success you edited!")
                return redirect('/')
            else:
                messages.error(request, "Username and password editing error!")
        except Exception as ex:
            print(ex)
            return redirect('/')
    else:
        form = User_Sing_Up_Form()
    return render(request, template_name='main/edit_user_datas.html', context={'form': form})


def sing_out(request):
    """It`s view for logout User"""
    logout(request)
    return redirect('/')


def create_category(request):
    """This view for creat new category"""
    if request.method == 'POST':
        form = Category_Form(data=request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations you`re created category!')
        else:
            messages.error(request, 'Category creation error!')
    else:
        form = Category_Form()
    return render(request, template_name='main/category_form.html', context={'form': form})


def create_article(request):
    """This view to create new article"""
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.user.id)
            form = Article_Form(request.POST or None, request.FILES or None)
            if form.is_valid():
                Article.objects.create(title=form.cleaned_data.get('title'),
                                       description=form.cleaned_data.get('description'),
                                       image=form.cleaned_data.get('image'),
                                       category_id=form.cleaned_data.get('category_id'),
                                       user_id=user).save()
                messages.success(request, 'Congratulations you`re created article!')
                return redirect('/')
            else:
                messages.error(request, 'Article creation error!')
        except Exception as ex:
            print(ex)
            return redirect('/')
    else:
        form = Article_Form()
    return render(request, template_name='main/create-article.html', context={'form': form})


def edit_article(request, article_id):
    """This view to edit article which was clicked by user to edit. User can edit only articles which was created by him."""
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=request.user.id)
            form = Article_Form(request.POST or None, request.FILES or None)
            if form.is_valid() and user.id == form.cleaned_data.get('user_id'):
                article = Article.objects.get(pk=article_id)
                article.title = form.cleaned_data.get('title')
                article.description = form.cleaned_data.get('description')
                article.image = form.cleaned_data.get('image')
                article.category_id = form.cleaned_data.get('category_id')
                article.user_id = user
                article.save()
                messages.success(request, 'Congratulations you`re edited article!')
                return redirect('/')
        except Exception as ex:
            print(ex)
            return redirect('/')
        else:
            messages.error(request, 'Article editing error!')
    else:
        form = Article_Form()
    return render(request, template_name='main/create-article.html', context={'form': form})


def delete_article(request, article_id):
    """This view to delete article which was clicked by user to delete. User can delete only articles which was created by him."""
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('/')
