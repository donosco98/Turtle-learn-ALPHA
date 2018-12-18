from django.contrib import admin
from django.urls import path,include,re_path
from . import views

from accounts.views import (login_view,register_view,logout_view)



app_name='quiz'

urlpatterns=[
     path('landing/',views.quiz_list),
     path('list/<int:id>', views.question_details),
     path('list/create',views.add_question,name="add"),
     path('list/image/<int:id>',views.add_image),
     path('list/quiz/<int:id>', views.quiz),
     path('list/quiz/get_data',views.data),
     path('list/quiz/get_data2',views.data2),


     path('register/',views.UserFormView.as_view()),
     path('login/',login_view),
     path('logout/',logout_view),
     path('list/quiz/submit/',views.result),


]
