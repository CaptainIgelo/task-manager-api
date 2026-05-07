from rest_framework.routers import DefaultRouter
from django.urls import path 
from .views import TaskViewSet, ping

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = router.urls + [
    path("ping/", ping, name="ping"),
]
