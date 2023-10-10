from rest_framework import serializers
from .models import Task

class ObjectIdField(serializers.Field):
    def to_representation(self, obj):
        return str(obj)

class TaskSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)  

    class Meta:
        model = Task
        fields = '__all__'
