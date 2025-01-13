from rest_framework import serializers
from ..models import Projects, Tasks, Team, TeamMembership


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

    def validate(self, data):
        if data.get('end_date') and data.get('start_date') and data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = '__all__'
