from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated


from issue.models import Issue
from api.serializers import IssueSerializer, IssueSerializerPatch


class IssueViewSet(
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet
                  ):
    permission_classes = (IsAuthenticated,)

    serializer_class = IssueSerializer
    serializer_class_patch = IssueSerializerPatch

    queryset = Issue.objects.all()


    def get_serializer_class(self):
        if self.request.method in ('PATCH',):
            return self.serializer_class_patch

        return self.serializer_class

    def get_queryset(self):
        state = self.request.GET.get('state')
        if (state != None):
            return Issue.objects.filter(state=state)
        return Issue.objects

