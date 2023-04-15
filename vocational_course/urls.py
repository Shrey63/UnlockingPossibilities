from django.urls import path


from django.contrib import admin
from django.urls import path
from vocational_course import views
urlpatterns = [
path('ProfessorSignIn',views.getProfessorSignIn),
path('ProfessorSignUp',views.getProfessorSignUp),
path('StudentSignIn',views.getStudentSignIn),
path('StudentSignUp',views.getStudentSignUp),
path('',views.home),
path('teacher',views.getTeacher),
path('contact',views.getContact),
path('about',views.getAbout),
path('posts',views.getPost),
path('courses',views.getCourses),
path('Logout',views.logout)]