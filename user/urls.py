# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.user_view, name='user-list'),  # <- 여기에 컴마 주의!
    path('user/follow/<int:id>/', views.user_follow, name='user-follow')

]