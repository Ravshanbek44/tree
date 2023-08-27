from rest_framework import generics
from .models import News, ForUsers
from .serializers import NewsSerializer, ForUserSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer


class NewsDetailAPIView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'


class ForUsersListAPIView(generics.ListAPIView):
    queryset = ForUsers.objects.all()
    serializer_class = ForUserSerializer

