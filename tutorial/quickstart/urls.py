from quickstart import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

router.register(r'log', views.LogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
