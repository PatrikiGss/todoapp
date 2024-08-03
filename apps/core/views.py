from datetime import date
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated # type: ignore
from rest_framework.authentication import SessionAuthentication, BasicAuthentication # type: ignore
from tasks.models import Task
from tasks.serializers import TaskSerializer

class HomeView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print('metodo da requisição', request.method)
        print('caminho da requisição', request.path)
        tasks = Task.objects.filter(end_date=date.today()).exclude(status='CD')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class SearchTasksView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        query = request.GET.get('query')
        tasks = Task.objects.filter(owner=request.user)
        if query:
            tasks = tasks.filter(name__icontains=query)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
