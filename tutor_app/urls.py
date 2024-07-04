from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tutor_app.views import TutorViewSet


router = DefaultRouter()
router.register(r'tutor', TutorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]