import datetime
from issue.models import Issue, IssueObject
from django.contrib.auth.models import User

def reset_issues():
    Issue.objects.update(state="Nuevo")

def create_issues(user):
    for tipo in dict(Issue.TYPE_CHOICES).values():
        issue = Issue.objects.create(
            user=user,
            type=tipo,
            description=tipo + " se quemó",
            issue_date=datetime.date.today(),
        )

        IssueObject.objects.create(
            issue=issue,
            name="(1) tipo: " + tipo,
            quantity=1,
            description="Incidente del objeto de tipo: " + tipo
        )

        IssueObject.objects.create(
            issue=issue,
            name="(2) tipo: " + tipo,
            quantity=1,
            description="Incidente del objeto de tipo: " + tipo
        )
        IssueObject.objects.create(
            issue=issue,
            name="(3) tipo: " + tipo,
            quantity=1,
            description="Incidente del objeto de tipo: " + tipo
        )


def fixture():
    user1 = User.objects.create(
        email="aseguradorassa+usuario1@gmail.com",
        username="usuario1",
        first_name="Nombre Usuario1",
        last_name="Apellido",
    )
    user1.set_password("123")
    user1.save()

    user2 = User.objects.create(
        email="aseguradorassa+usuario2@gmail.com",
        username="usuario2",
        first_name="Carlos",
        last_name="Apellido",
    )
    user2.set_password("123")
    user2.save()

    user3 = User.objects.create(
        email="aseguradorassa+usuario3@gmail.com",
        username="usuario3",
        first_name="Nombre Usuario2",
        last_name="Apellido",
    )
    user3.set_password("123")
    user3.save()

    user4 = User.objects.create(
        email="aseguradorassa+usuario4@gmail.com",
        username="usuario4",
        first_name="Nombre Usuario4",
        last_name="Apellido",
    )
    user4.set_password("123")
    user4.save()

    admin = User.objects.create(
        email="admin@admin.com",
        username="admin",
        first_name="admin",
        last_name="admin",
        is_staff=True,
    )
    admin.set_password("123")
    admin.save()

    create_issues(user1)
    create_issues(user2)
    create_issues(user3)
    create_issues(user4)

