from django.urls import path
from users import views
from django.urls import path ,include


#app_name = 'users'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name="contact"),
]