from django.urls import path


from django.contrib import admin
from django.urls import path
from vocational_course import views
urlpatterns = [
#just get all the 4 forms
path('ProfessorSignInPage',views.getProfessorSignInPage),
path('ProfessorSignUpPage',views.getProfessorSignUpPage),
path('StudentSignInPage',views.getStudentSignInPage),
path('StudentSignUpPage',views.getStudentSignUpPage),

path('',views.home),

#action of all the 4 forms
path('getSignedUp',views.getCanSignedUp),
path('getSignedIn',views.getCanSignedIn),
path('getProfSignedUp',views.getProfSignedUp),
path('getProfSignedIn',views.getProfSignedIn),


path('teacher',views.getTeacher),
path('contact',views.getContact),
path('about',views.getAbout),
path('posts',views.getPost),
path('courses',views.getCourses),
path('Logout',views.logout)]