from django.urls import  path
from web_film import  views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Book_list_view.as_view(), name='index'),
    path('help/', views.Help.as_view(), name='help'),
    path('about_me/', views.About_me.as_view(), name='about_me'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('my_account/', views.My_account.as_view(), name='my_account'),
    path('logout/', views.logout, name='logout'),
    path('change_password/',  views.Change_password.as_view(), name='change_password'),
    path('forgot_password/', views.Forgot_password.as_view(), name='forgot_password'),
    path('question/<int:pk>/', views.Question_view.as_view(), name='question'),
    path('question_api/', views.Create_view.as_view(), name='create_question'),
    path('question_api/<int:pk>/', views.DeailsView.as_view(), name='detail_question'),
    path('question_api/<int:pk>/choices/', views.Choice_list.as_view(), name='detail_answer_of_question'),
]

urlpatterns = format_suffix_patterns(urlpatterns)