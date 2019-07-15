from rest_framework import serializers, routers
from .models import Experiment, ExperimentVote, ExperimentComment, ExperimentCommentVote


# Serializer definitions
class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'


class ExperimentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentVote
        fields = '__all__'


# Serializer definitions
class ExperimentCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'


class ExperimentCommentVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentVote
        fields = '__all__'
