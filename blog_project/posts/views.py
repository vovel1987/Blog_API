from django.shortcuts import render
from rest_framework import generics, permissions,viewsets
from django.contrib.auth import get_user_model
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    permission_classes =(IsAuthorOrReadOnly)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class =UserSerializer



class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes =(IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class =UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# Create your views here.
