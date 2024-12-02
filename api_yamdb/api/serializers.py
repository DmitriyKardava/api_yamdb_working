from rest_framework import serializers

from review_user.models import ReviewUser
from reviews.models import Category, Genre, Title


class ReviewUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = ReviewUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Title
