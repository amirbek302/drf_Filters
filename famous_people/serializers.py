from rest_framework import serializers
from .models import FamousPeopleModel

class FamousPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamousPeopleModel
        fields = ['id', 'title', 'text']
        read_only_fields = ['id']
