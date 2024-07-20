from django.urls import path
from . import views

urlpatterns = [
    path ('' , views.shows_list , name ='show_list'),
    path('show_new',views.show_new,name='show_new'),
    path ('show_detail/<int:id>/', views.show_det,name='show_detail'),
    path('show_edit/<int:id>/', views.show_edit, name='show_edit'),
    path('confirm_delete/<int:id>/', views.confirm_delete ,name='confirm_delete'),
    path('show_delete', views.show_delete ,name='show_delete'),

]
