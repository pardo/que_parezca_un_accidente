from django.db import models
from django.contrib.auth.models import User, Group


class Issue(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    TYPE_CHOICES = (
        ("Casa", "Casa"),
        ("Objeto", "Objeto"),
        ("Auto", "Auto")
    )

    user = models.ForeignKey(User)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default="Objeto")
    description = models.TextField(default="")


class IssueObject(models.Model):
    issue = models.ForeignKey(Issue)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(default="")
