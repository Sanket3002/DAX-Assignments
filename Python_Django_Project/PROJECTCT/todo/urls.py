from django.urls import path
from . import views
urlpatterns = [
   path('',views.task_list,name='task_list'),
   path('task/<int:id>/',views.task_detail,name ='task_detail'),
   path('task/new/',views.task_new,name='task_new'),
   path('task/<int:id>/edit/',views.task_edit,name = 'task_edit'),
   # path('task/<int:id>/detail_update/',views.task_detail,name ='task_detail'),
   path('task/<int:id>/detail_update/',views.task_detail_update,name = 'task_detail_update'),
   path('task/<int:id>/delete/',views.task_delete,name = 'task_delete')

]
 