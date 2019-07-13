from django.conf.urls import url, include
from rest_framework import serializers, routers
from .models import Study, StudyVote, StudyThread, StudyThreadVote, StudyComment, StudyCommentVote


# Serializer definitions
class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = '__all__'


class StudyVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyVote
        fields = '__all__'


class StudyThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyThread
        fields = '__all__'


class StudyThreadVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyThreadVote
        fields = '__all__'


class StudyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyComment
        fields = '__all__'


class StudyCommentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyCommentVote
        fields = '__all__'
