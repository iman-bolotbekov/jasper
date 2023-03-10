from django.urls import path, include
from rest_framework import routers
from . import views as iman_views

router = routers.DefaultRouter()
router.register('text', iman_views.Numbo_textViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]