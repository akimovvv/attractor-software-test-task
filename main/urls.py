from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('my-profile/', get_all_user_data, name='my_profile'),
    path('category/<int:category_id>/', get_articles_by_category, name='get_articles_by_category_id'),
    path('sing-in/', sing_in, name='sing_in'),
    path('sing-up/', sing_up, name='sing_up'),
    path('sing-out/', sing_out, name='sing_out'),
    path('edit-user/', edit_user, name='edit_user'),
    path('create-category/', create_category, name='create_category'),
    path('create-article/', create_article, name='create_article'),
    path('edit-article/<int:article_id>/', edit_article, name='edit_article'),
    path('delete-article/<int:article_id>/', delete_article, name='delete_article')
]
