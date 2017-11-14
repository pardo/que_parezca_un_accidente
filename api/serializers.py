from rest_framework import serializers

from issue.models import Issue, IssueObject


class IssueObjectSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        attrs["issue"] = self.context.get("issue")
        return attrs

    class Meta:
        model = IssueObject
        fields = (
            "name",
            "quantity",
            "description"
        )


class IssueSerializer(serializers.ModelSerializer):
    objects = IssueObjectSerializer(source="get_objects", many=True)
    url = serializers.CharField(source="get_unique_url", read_only=True)

    class Meta:
        model = Issue
        fields = (
            'id',
            'type',
            'description',
            'objects',
            'issue_date',
            'uuid',
            'state',
            'tomado_date',
            'visado_date',
            'revisado_date',
            'aprobado_date',
            'desaprobado_date',
            'url'
        )
        read_only = (
            'uuid',
            'tomado_date',
            'visado_date',
            'revisado_date',
            'aprobado_date',
            'desaprobado_date',
        )


    def validate(self, attrs):
        if self.instance is None:
            attrs["user"] = self.context["request"].user
        return attrs

    def create(self, validated_data):
        objects = validated_data.pop("get_objects")

        instance = Issue.objects.create(**validated_data)

        objects_serializer = IssueObjectSerializer(
            data=objects,
            context={ "issue": instance },
            many=True
        )

        objects_serializer.is_valid()
        objects_serializer.save()

        return instance


class IssueSerializerPatch(serializers.ModelSerializer):
    def get_data(self):
        return IssueSerializer(self.instance, context=self.context).data

    def set_data(self, val):
        pass

    data = property(get_data, set_data)

    class Meta:
        model = Issue
        fields = (
            'type',
            'state',
        )
        read_only = (
            'uuid',
        )

        write_only = (
            'type',
            'state',
        )


