from django.urls import path


from django.contrib import admin
from django.urls import path
from vocational_course import views
urlpatterns = [
path('',views.getProffLoginPage),
# path('LogIn',views.userLogin),
# path('', views.home),
path('Logout',views.logout)
# path('home', views.home, name='home'),
]