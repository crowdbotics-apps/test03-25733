from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ForwardedMessageViewSet,
    MessageViewSet,
    ThreadMemberViewSet,
    MessageActionViewSet,
    ThreadViewSet,
    ThreadActionViewSet,
)

router = DefaultRouter()
router.register("threadmember", ThreadMemberViewSet)
router.register("messageaction", MessageActionViewSet)
router.register("threadaction", ThreadActionViewSet)
router.register("message", MessageViewSet)
router.register("forwardedmessage", ForwardedMessageViewSet)
router.register("thread", ThreadViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
