from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from issue.models import Issue
from api.serializers import IssueSerializer


class IssueViewSet(
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet
                  ):
    permission_classes = (IsAuthenticated,)
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

    def get_queryset(self):
        return Issue.objects.filter(user=self.request.user)
