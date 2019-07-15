from rest_framework import routers
from .views import ExperimentViewSet, ExperimentVoteViewSet, ExperimentCommentViewSet, ExperimentCommentVoteViewSet


# Route definitions
router = routers.DefaultRouter()
router.register(r'experiment', ExperimentViewSet)
router.register(r'experiment-vote', ExperimentVoteViewSet)
router.register(r'experiment-comment', ExperimentCommentViewSet)
router.register(r'experiment-comment-vote', ExperimentCommentVoteViewSet)
