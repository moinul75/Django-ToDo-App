from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.Home, name='todo'),
    path('mark_as_done/<int:pk>',views.mard_as_done,name='mark_as_done'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('undo_task/<int:pk>',views.undo_task,name='mark_as_undo'),
    path('get-task-content/<int:task_id>/', views.get_task_content, name='get_task_content'),
    path('update_task/<int:task_id>/',views.update_task, name='update_task'),
]
