from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny #IsAuthenticatedOrReadOnly
#IsAuthenticated

from issue.models import Issue
from api.serializers import IssueSerializer


class IssueViewSet(
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet
                  ):
    permission_classes = (AllowAny,)
#(IsAuthenticated,)
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

    def get_queryset(self):
        state = self.request.GET.get('state')
        if (state != None):
            return Issue.objects.filter(state=state)
        return Issue.objects
