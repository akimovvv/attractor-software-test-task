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
    path('delete-article/<int:article_id>/', delete_article, name='delete_article'),


    path('api/get-all-category/', List_Category_Api_View.as_view(), name='api_get_all_category'),
    path('api/create-category/', Create_Category_Api_View.as_view(), name='api_create_category'),
    path('api/update-category/<int:pk>/', Update_Category_Api_View.as_view(), name='api_update_category'),
    path('api/delete-category/<int:pk>/', Delete_Category_Api_View.as_view(), name='api_delete_category'),


    path('api/get-all-article/', List_Article_Api_View.as_view(), name='api_get_all_article'),
    path('api/create-article/', Create_Article_Api_View.as_view(), name='api_create_article'),
    path('api/update-article/<int:pk>/', Update_Article_Api_View.as_view(), name='api_update_article'),
    path('api/delete-article/<int:pk>/', Delete_Article_Api_View.as_view(), name='api_delete_article'),

]
