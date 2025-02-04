from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .views import custom_login

urlpatterns = [
    path('index',views.index,name='index'),
    path('manage_department',views.manage_department,name='manage_department'),
    path('add_department',views.add_department,name='add_department'),
    path('edit_department/<int:pk>',views.edit_department,name='edit_department'),
    path('delete_department/<int:pk>',views.delete_department,name='delete_department'),
    
    path('manage_program', views.manage_program, name='manage_program'),
    path('add_program',views.add_program,name='add_program'),
    path('edit_program/<int:pk>',views.edit_program,name='edit_program'),
    path('delete_program/<int:pk>',views.delete_program,name='delete_program'),

    path('manage_students/', views.manage_student, name='manage_student'),  # View all students
    path('students/add/', views.add_student, name='add_student'),  # Add student
    path('students/edit/<int:student_id>/', views.edit_student, name='edit_student'),  # Edit student
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),  # Delete student


    path('manage_scholarships/', views.manage_scholarship, name='manage_scholarship'),  # View all scholarships
    path('scholarships/add/', views.add_scholarship, name='add_scholarship'),  # Add new scholarship
    path('scholarships/edit/<int:pk>/', views.edit_scholarship, name='edit_scholarship'),  # Edit scholarship
    path('scholarships/delete/<int:pk>/', views.delete_scholarship, name='delete_scholarship'),  # Delete scholarship
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('student_scholarships/add/', views.add_student_scholarship, name='add_student_scholarship'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', custom_login, name='login'),

    path('transfer-certificates/', views.transfer_certificate_list, name='transfer_certificate_list'),
    path('add-transfer-certificate/', views.add_transfer_certificate, name='add_transfer_certificate'),
    path('edit-transfer-certificate/<int:tc_id>/', views.edit_transfer_certificate, name='edit_transfer_certificate'),
    path('delete-transfer-certificate/<int:tc_id>/', views.delete_transfer_certificate, name='delete_transfer_certificate'),

]
  