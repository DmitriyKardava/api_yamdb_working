from rest_framework import serializers

from review_user.models import ReviewUser
from reviews.models import Category, Comment, Genre, Title


class ReviewUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = ReviewUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        'category', many=True, read_only=True)

    class Meta:
        fields = ('__all__')
        model = Title


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
