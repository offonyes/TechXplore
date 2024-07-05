from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

from tutor_app.views import TutorViewSet, CityListView, SubjectListView


router = DefaultRouter()
router.register(r'tutor', TutorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/cities/', CityListView.as_view(), name='city-list'),
    path('api/subjects/', SubjectListView.as_view(), name='')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)