from django.db import models
from N1.models import UserCreated
from datetime import datetime


class Study(UserCreated):
    name = models.CharField(max_length=255)
    field = models.CharField(max_length=255)
    description = models.TextField()
    hypothesis = models.TextField()
    hypothesis_updated_date = models.DateTimeField(default=datetime.now)

    @property
    def votes(self):
        return len(StudyVote.objects.filter(study=self.id))


class StudyVote(UserCreated):
    study = models.ForeignKey(to=Study, on_delete=models.CASCADE)


class StudyThread(UserCreated):
    name = models.CharField(max_length=255)
    study = models.ForeignKey(to=Study, on_delete=models.CASCADE)

    @property
    def votes(self):
        return len(StudyThreadVote.objects.filter(study_thread=self.id))


class StudyThreadVote(UserCreated):
    study_thread = models.ForeignKey(to=StudyThread, on_delete=models.CASCADE)


class StudyComment(UserCreated):
    study_thread = models.ForeignKey(to=StudyThread, on_delete=models.CASCADE)
    comment_body = models.TextField()

    @property
    def votes(self):
        return len(StudyComment.objects.filter(study_comment=self.id))


class StudyCommentVote(UserCreated):
    study_comment = models.ForeignKey(to=StudyComment, on_delete=models.CASCADE)




