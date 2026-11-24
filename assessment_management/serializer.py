from rest_framework import serializers

from assessment_management.models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Assessment

        fields = "__all__"

        read_only_fields = ["id","tutor","slug","created_at","updated_at"]