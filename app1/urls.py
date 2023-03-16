from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index, name='homepage'),
    path('goals/<int:pk>/',views.goals, name='goals'),
    path('sleeplogger',views.sleeplogger,name='sleeplogger'),
    path('leetcode', views.leetcode_list, name='leetcode'),
    path('create-task', views.createTask, name='create-task'),
    path('update-task/<str:pk>', views.updateTask, name='updatetask'),
    
    
]