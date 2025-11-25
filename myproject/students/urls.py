from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('statfiles/', views.static_files, name='static_files'),
    re_path(r'^student/(?P<student_id>\d+)/$', views.student_detail, name='student_detail'),
    path('search/', views.search_student, name='search_student'),
    path('formhtml/', views.form_html, name='form_html'),
    path('formhtml/result/', views.form_html_result, name='form_html_result'),
    path('students/', views.students_list, name='students_list'),
    path('fields/', views.fields, name='fields'),
    path('userdata/', views.userdata, name='userdata'),
]