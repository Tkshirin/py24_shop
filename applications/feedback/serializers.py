from rest_framework import serializers

from applications.feedback.models import Comment, Favorite, Like, Rating


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Comment
        fields = '__all__'
