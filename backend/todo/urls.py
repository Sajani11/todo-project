from django.contrib import admin
from django.urls import path, include
from todo.views import TodoListCreate, TodoRetrieveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', TodoListCreate.as_view(), name='todo-list-create'),
    path('api/tasks/<int:pk>/', TodoRetrieveUpdateDestroy.as_view(), name='todo-retrieve-update-destroy'),
]
