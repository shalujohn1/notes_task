from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Project

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET': '/api/projects'},
        {'GET': '/api/projects/id'},

        {'POST': '/api/projects/token'},
        {'POST': '/api/projects/token/refresh'}
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def add_Project(request):
    add_project = Project.objects.create(
        title=request.data['title'],
        description=request.data['description'],
        )
    serializer = ProjectSerializer(add_project, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_Project(request, pk):
    project = Project.objects.get(id=pk)
    project.title = request.data['title']
    project.description = request.data['description']
    project.save()
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_Project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return Response("successfully deleted")


