from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True}
        }

    def validate_status(self, value):
        allowed_statuses = [
            "Applied",
            "Shortlisted",
            "Interview",
            "Selected",
            "Rejected",
            "Withdrawn",
        ]

        if value not in allowed_statuses:
            raise serializers.ValidationError(
                "Invalid status. Choose a valid application status."
            )

        return value