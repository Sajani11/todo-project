from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# List all Todos or create a new Todo
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Retrieve, update or delete a Todo
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
