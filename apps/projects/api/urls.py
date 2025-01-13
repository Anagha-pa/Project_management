from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import ProjectAPIView, TaskViewSet, TeamViewSet, TeamMembershipViewSet

# Routers for ViewSets
router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
router.register('teams', TeamViewSet, basename='teams')
router.register('team-memberships', TeamMembershipViewSet, basename='team-memberships')

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="Project Management API",
        default_version="v1",
        description="API for managing projects, tasks, teams, and team memberships.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Project APIView
    path('projects/', ProjectAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectAPIView.as_view(), name='project-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
]
