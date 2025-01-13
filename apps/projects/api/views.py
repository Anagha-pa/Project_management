from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Projects, Tasks, Team, TeamMembership
from .serializers import ProjectSerializer, TaskSerializer, TeamSerializer, TeamMembershipSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ProjectAPIView(APIView):

    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        responses={200: ProjectSerializer(many=True)},
        operation_description="Retrieve all projects or a specific project by ID.",
    )
    
    def get(self, request, pk=None):
        if pk:
            try:
                project = Projects.objects.get(pk=pk)
                serializer = ProjectSerializer(project)
                return Response(serializer.data)
            except Projects.DoesNotExist:
                return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


    @swagger_auto_schema(
        request_body=ProjectSerializer,
        responses={201: ProjectSerializer, 400: "Bad Request"},
        operation_description="Create a new project with details such as name, description, start_date, end_date, and status.",
    )
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        request_body=ProjectSerializer,
        responses={200: ProjectSerializer, 400: "Bad Request", 404: "Not Found"},
        operation_description="Update an existing project by ID.",
    )
    def put(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        responses={204: "No Content", 404: "Not Found"},
        operation_description="Delete a project by ID.",
    )
    def delete(self, request, pk=None):
        try:
            project = Projects.objects.get(pk=pk)
            project.delete()
            return Response({"message": "Project deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Projects.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)



class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamMembershipViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
