from rest_framework import viewsets
from .models import Experiment, ExperimentVote, ExperimentComment, ExperimentCommentVote
from .serializers import ExperimentSerializer, ExperimentVoteSerializer, ExperimentCommentSerializer, \
    ExperimentCommentVoteSerializer


# ViewSet definitions
class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer


class ExperimentVoteViewSet(viewsets.ModelViewSet):
    queryset = ExperimentVote.objects.all()
    serializer_class = ExperimentVoteSerializer


class ExperimentCommentViewSet(viewsets.ModelViewSet):
    queryset = ExperimentComment.objects.all()
    serializer_class = ExperimentCommentSerializer


class ExperimentCommentVoteViewSet(viewsets.ModelViewSet):
    queryset = ExperimentCommentVote.objects.all()
    serializer_class = ExperimentCommentVoteSerializer
