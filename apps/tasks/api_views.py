from rest_framework import status# type: ignore
from rest_framework.views import APIView# type: ignore
from rest_framework.response import Response# type: ignore
from rest_framework.permissions import IsAuthenticated# type: ignore
from django.shortcuts import get_object_or_404# type: ignore
from django.contrib import messages# type: ignore
from .models import Category, Task
from .forms import CategoryForms, TaskForm
from .serializers import CategorySerializer, TaskSerializer

class AddCategoryAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request):
        form = CategoryForms(request.data)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCategoriesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = Category.objects.filter(owner=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id_category):
        category = get_object_or_404(Category, id=id_category, owner=request.user)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id_category):
        category = get_object_or_404(Category, id=id_category)
        if category.owner == request.user:
            category.delete()
            messages.success(request, 'Categoria excluída com sucesso.')
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            messages.error(request, 'Você não tem permissão para excluir esta categoria.')
            return Response(status=status.HTTP_403_FORBIDDEN)

class AddTaskAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        form = TaskForm(request.data)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form.save_m2m()
            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

class ListTasksAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.filter(owner=request.user).exclude(status='CD')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditTaskAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id_task):
        task = get_object_or_404(Task, id=id_task, owner=request.user)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTaskAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id_task):
        task = get_object_or_404(Task, id=id_task)
        if task.owner == request.user:
            task.delete()
            messages.success(request, 'Tarefa excluída com sucesso.')
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            messages.error(request, 'Você não tem permissão para excluir esta tarefa.')
            return Response(status=status.HTTP_403_FORBIDDEN)
