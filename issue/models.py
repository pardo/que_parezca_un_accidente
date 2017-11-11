import uuid

from django.db import models
from django.contrib.auth.models import User, Group

class Issue(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    TYPE_CHOICES = (
        ("Casa", "Casa"),
        ("Objeto", "Objeto"),
        ("Auto", "Auto")
    )

    user = models.ForeignKey(User)
    issue_date = models.DateField()
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default="Objeto")
    description = models.TextField(default="")

    def get_objects(self):
        return self.issueobject_set.all()

    @classmethod
    def get_by_uuid(self, uuid):
        return Issue.objects.first() #TODO

class IssueObject(models.Model):
    issue = models.ForeignKey(Issue)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(default="")
