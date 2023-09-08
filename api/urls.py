from django.urls import path
from .import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    path('projects/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('projects/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('add_project/', views.add_Project),
    path('update_project/<str:pk>/', views.update_Project),
    path('delete_project/<str:pk>/', views.delete_Project),

    path('projects/<str:pk>/', views.getProject),

]