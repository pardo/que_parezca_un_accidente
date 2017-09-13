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

    def validate(self, attrs):
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

    class Meta:
        model = Issue
        fields = (
            'type',
            'description',
            'objects'
        )
