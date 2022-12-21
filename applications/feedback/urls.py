from rest_framework.routers import DefaultRouter
from django.urls import path, include

from applications.feedback.views import CommentAPIView

router = DefaultRouter()
router.register('comment', CommentAPIView)

urlpatterns = [
    path('', include(router.urls)),
]