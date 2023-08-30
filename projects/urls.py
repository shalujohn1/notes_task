from django.urls import path
from.import views


urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create=project/', views.createProject,name="create-Project"),
    path('update-project/<str:pk>/', views.updateProject,
         name="update-project"),
    path('delete-project/<str:pk>',views.deleteProject,name="delete-project"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    ]

