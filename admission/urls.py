from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('manage_department',views.manage_department,name='manage_department'),
    path('add_department',views.add_department,name='add_department'),
    path('edit_department/<int:pk>',views.edit_department,name='edit_department'),
    path('delete_department/<int:pk>',views.delete_department,name='delete_department'),
]