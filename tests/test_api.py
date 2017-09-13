import json

from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client


class IssueTest(TestCase):
    def login(self):
        self.client.login(username=self.user.email, password='pass')

    def create_user_test(self):
        user = User.objects.create(
            email="test@test.com",
            username="test@test.com",
            is_active=True
        )
        user.set_password('pass')
        user.save()
        self.user = user
        return user

    def setUp(self):
        self.create_user_test()
        self.client = Client()


    def test_create_issue(self):
        self.login()

        data = {
            "description": "issue description",
            "type": "Casa",
            "objects": [
                {
                    "name": "obj name 1",
                    "quantity": 1,
                    "description": "fallo",
                }, {
                    "name": "obj name 1",
                    "quantity": 1,
                    "description": "fallo",
                }
            ]
        }

        response = self.client.post(
            reverse('issue-list'),
            data=json.dumps(
                data
            ),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
