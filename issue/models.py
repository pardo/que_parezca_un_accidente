import datetime
import uuid

from decimal import Decimal
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User, Group
from django.urls.base import reverse


class Issue(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    TYPE_CHOICES = (
        ("Casa", "Casa"),
        ("Objeto", "Objeto"),
        ("Auto", "Auto")
    )

    STATES = (
        ("Nuevo", "Nuevo"),
        ("Tomado", "Tomado"),
        ("Visado", "Visado"),
        ("Presupuestado", "Presupuestado"),
        ("Aprobado", "Aprobado"),
        ("Desaprobado", "Desaprobado")
    )

    user = models.ForeignKey(User)
    issue_date = models.DateField()

    visado_date = models.DateField(null=True, blank=True)
    revisado_date = models.DateField(null=True, blank=True)
    tomado_date = models.DateField(null=True, blank=True)
    aprobado_date = models.DateField(null=True, blank=True)
    desaprobado_date = models.DateField(null=True, blank=True)

    type = models.CharField(max_length=255, choices=TYPE_CHOICES, default="Objeto")
    state = models.CharField(max_length=255, choices=STATES, default="Nuevo")
    description = models.TextField(default="")
    monto = models.DecimalField(decimal_places=2, max_digits=10, default=Decimal("0.0"))
    case_id = models.CharField(max_length=30, default="")

    def get_objects(self):
        return self.issueobject_set.all()

    @classmethod
    def get_by_uuid(self, uuid):
        return Issue.objects.first() #TODO

    def get_unique_url(self):
        return settings.DOMAIN + reverse("issue_view", args=[self.uuid])

    def save(self, *args, **kwargs):
        if self.state == "Tomado" and self.tomado_date is None:
            self.tomado_date = datetime.date.today()
        if self.state == "Visado" and self.visado_date is None:
            self.visado_date = datetime.date.today()
        if self.state == "Revisado" and self.revisado_date is None:
            self.revisado_date = datetime.date.today()
        if self.state == "Aprobado" and self.aprobado_date is None:
            self.aprobado_date= datetime.date.today()
        if self.state == "Desaprobado" and self.desaprobado_date is None:
            self.desaprobado_date = datetime.date.today()

        return super(Issue, self).save(*args, **kwargs)

class IssueObject(models.Model):
    issue = models.ForeignKey(Issue)
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(default="")
