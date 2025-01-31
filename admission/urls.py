from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
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


    
]
  