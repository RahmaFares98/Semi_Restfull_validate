from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new_show, name='new_show'),
    path('create', views.create, name='create_show'),  # Assuming your view function is named 'create'
    path('<int:id>', views.show_detail, name='show_detail'),
    path('', views.shows_list, name='shows_list'),
    path('<int:id>/edit', views.edit_show, name='edit_show'),
    path('<int:id>/update', views.update_show, name='update_show'),
    path('<int:id>/destroy', views.destroy_show, name='destroy_show'),
    path('check_unique_title/', views.check_unique_title, name='check_unique_title'),
]
