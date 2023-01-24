from django.urls import path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout'),
    ]