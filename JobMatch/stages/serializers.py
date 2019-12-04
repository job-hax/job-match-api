from django.db.models import Count
from rest_framework import serializers

from .models import Stage

class StageBasicsSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Stage.objects.create(**validated_data)

    class Meta:
        model = Stage
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Stage.objects.create(**validated_data)

    class Meta:
        model = Stage
        fields = ('__all__')
