import datetime
from issue.models import Issue, IssueObject
from django.contrib.auth.models import User


def reset():
    Issue.objects.update(state="Nuevo")


def fixture():
    for tipo in dict(Issue.TYPE_CHOICES).values():
        issue = Issue.objects.create(
            user=User.objects.first(),
            type=tipo,
            description=tipo + " quemada",
            issue_date=datetime.date.today(),
        )

        IssueObject.objects.create(
            issue=issue,
            name="Lorem " + tipo,
            quantity=1,
            description="Lorem " + tipo
        )

        IssueObject.objects.create(
            issue=issue,
            name="Ipsum " + tipo,
            quantity=1,
            description="Ipsum " + tipo
        )
        IssueObject.objects.create(
            issue = issue,
            name="Dolor " + tipo,
            quantity=1,
            description="Dolor " + tipo
        )


