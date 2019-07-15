from rest_framework import routers
from .views import StudyViewSet, StudyVoteViewSet, StudyThreadViewSet, StudyThreadVoteViewSet, StudyCommentViewSet, \
    StudyCommentVoteViewSet


# Route definitions
router = routers.DefaultRouter()
router.register(r'study', StudyViewSet)
router.register(r'study-vote', StudyVoteViewSet)
router.register(r'study-thread', StudyThreadViewSet)
router.register(r'study-thread-vote', StudyThreadVoteViewSet)
router.register(r'study-comment', StudyCommentViewSet)
router.register(r'study-comment-vote', StudyCommentVoteViewSet)
