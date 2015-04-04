from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from rest_app.models import Post
from django.http import Http404
from django.contrib import auth
from django.contrib.auth.models import User

from rest_app.serializers import PostSerializer, PostSerializerList, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


def index(request):
    args = {}
    args.update(csrf(request))
    # posts = Post.objects.all()
    # context = {'posts': posts}
    # template = "rest_app/index.html"
    args['posts'] = Post.objects.all()
    args['username'] = auth.get_user(request).username
    return render_to_response("rest_app/index.html", args)


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostList(APIView):

    '''
    List all posts, or create a new post.
    '''
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializerList(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializerList(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostDetail(APIView):
    """
    Retrieve, update or delete a post instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        post = PostSerializer(post)
        return Response(post.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)