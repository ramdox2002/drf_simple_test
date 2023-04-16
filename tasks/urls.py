from django.urls import path
import tasks.views as v
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register("api/projects" , ProjectViewSet , "projects")

urlpatterns = router.urls
