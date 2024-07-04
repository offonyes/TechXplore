from django.urls import path
from accounts_app.views import RegisterView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
]
