from django.db import models
from N1.models import UserCreated
from Study.models import Study


class Experiment(UserCreated):
    name = models.CharField(max_length=255)
    study = models.ForeignKey(to=Study, on_delete=models.CASCADE)
    content = models.TextField()

    @property
    def votes(self):
        return len(ExperimentVote.objects.filter(experiment=self.id))


class ExperimentVote(UserCreated):
    experiment = models.ForeignKey(to=Experiment, on_delete=models.CASCADE)


class ExperimentComment(UserCreated):
    comment_body = models.TextField()

    @property
    def votes(self):
        return len(ExperimentCommentVote.objects.filter(experiment_comment=self.id))


class ExperimentCommentVote(UserCreated):
    experiment_comment = models.ForeignKey(to=ExperimentComment, on_delete=models.CASCADE)


