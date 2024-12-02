# from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404

from rest_framework import filters, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken


from reviews.models import Category, Genre, Title
from review_user.models import ReviewUser
from .permissions import AdminUserOrReadOnly
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleSerializer,
                          ReviewUserSerializer,)


class ReviewUserViewSet(viewsets.ModelViewSet):
    queryset = ReviewUser.objects.all()
    serializer_class = ReviewUserSerializer


class CategoryViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AdminUserOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class TokenAPIView(APIView):
    permission_classes = (AllowAny,)

    # @swagger_auto_schema(request_body=TokenSerializer())
    def post(self, request):
        # serializer = TokenSerializer(data=request.data)

        # serializer.is_valid(raise_exception=True)
        user = get_object_or_404(ReviewUser, username=request.data["username"])
        # if not default_token_generator.check_token(
        #     user,
        #     serializer.data["confirmation_code"],
        # ):
        #     raise ValidationError("Неверный код")

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        token = dict(token=access_token)
        return Response(token)
