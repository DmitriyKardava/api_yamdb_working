from rest_framework import viewsets

from reviews.models import Category, Genre, Title
from review_user.models import ReviewUser
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          ReviewUserSerializer,)


class ReviewUserViewSet(viewsets.ModelViewSet):
    queryset = ReviewUser.objects.all()
    serializer_class = ReviewUserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
