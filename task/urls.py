from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_task, name='add-task'),
    path('update/<int:pk>', views.update_task, name='update-task'),
    path('delete/<int:pk>', views.delete_task, name='delete-task'),
]
