from snippets import serializers
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
#mixin views....!
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
     queryset = Snippet.objects.all()
     serializer_class = SnippetSerializer

     def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

     def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

     def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
     

# Generic views...!
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer     


#End Points views from serializers


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    