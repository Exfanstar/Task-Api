from .models import Task, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    coms = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
