from django.contrib import admin
from issue.models import Issue, IssueObject

admin.site.register(Issue)
admin.site.register(IssueObject)
