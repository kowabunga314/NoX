from rest_framework import routers
from .views import StudyViewSet, StudyVoteViewSet, StudyThreadViewSet, StudyThreadVoteViewSet, StudyCommentViewSet, \
    StudyCommentVoteViewSet
from django.urls import include
from django.conf.urls import url


# Route definitions
router = routers.DefaultRouter()
router.register(r'', StudyViewSet)
router.register(r'vote/', StudyVoteViewSet)
router.register(r'thread', StudyThreadViewSet)
router.register(r'thread-vote', StudyThreadVoteViewSet)
router.register(r'comment', StudyCommentViewSet)
router.register(r'comment-vote', StudyCommentVoteViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'study', include(router.urls)),
# ]
