from rest_app.models import Post, User

from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'time')



class PostSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'time')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (id)