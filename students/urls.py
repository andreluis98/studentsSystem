from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_students, name='view_students'),
    path('add', views.add_students, name='add_students'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
