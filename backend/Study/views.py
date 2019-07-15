from rest_framework import viewsets
from .models import Study, StudyVote, StudyThread, StudyThreadVote, StudyComment, StudyCommentVote
from .serializers import StudySerializer, StudyVoteSerializer, StudyThreadSerializer, StudyThreadVoteSerializer, \
    StudyCommentSerializer, StudyCommentVoteSerializer


# ViewSet definitions
class StudyViewSet(viewsets.ModelViewSet):
    queryset = Study.objects.all()
    serializer_class = StudySerializer


class StudyVoteViewSet(viewsets.ModelViewSet):
    queryset = StudyVote.objects.all()
    serializer_class = StudyVoteSerializer


class StudyThreadViewSet(viewsets.ModelViewSet):
    queryset = StudyThread.objects.all()
    serializer_class = StudyThreadSerializer


class StudyThreadVoteViewSet(viewsets.ModelViewSet):
    queryset = StudyThreadVote.objects.all()
    serializer_class = StudyThreadVoteSerializer


class StudyCommentViewSet(viewsets.ModelViewSet):
    queryset = StudyComment.objects.all()
    serializer_class = StudyCommentSerializer


class StudyCommentVoteViewSet(viewsets.ModelViewSet):
    queryset = StudyCommentVote.objects.all()
    serializer_class = StudyCommentVoteSerializer
