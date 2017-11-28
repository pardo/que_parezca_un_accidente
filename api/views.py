import requests

from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

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

    def check_permissions(self, request):
        if "pk" in self.kwargs:
            try:
                return Issue.objects.get(uuid=self.kwargs["pk"])
            except Exception:
                pass
        return super(IssueViewSet, self).check_permissions(request)

    def get_object(self):
        if "pk" in self.kwargs:
            try:
                return Issue.objects.get(uuid=self.kwargs["pk"])
            except Exception:
                pass
        return super(IssueViewSet, self).get_object()

    def get_queryset(self):
        state = self.request.GET.get('state')
        case_id = self.request.GET.get('case_id')

        if self.request.user.is_staff:
            qs = Issue.objects.all()

            if state is not None:
                qs = qs.filter(state=state)

            if case_id is not None:
                qs = qs.filter(case_id=case_id)

            return qs

        return Issue.objects.filter(user=self.request.user)

    @detail_route(methods=["get"])
    def images(self, *args, **kwargs):
        issue = self.get_object()
        r = requests.get("https://dssd-grupo26.herokuapp.com/upload/?metadata=%s" % issue.id)
        try:
            data = r.json()
            return Response(list(map(lambda x: x["link"], data)))
        except Exception:
            return Response([])