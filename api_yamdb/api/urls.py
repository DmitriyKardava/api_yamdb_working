from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (CategoryViewSet,
                       GenreViewSet,
                       TitleViewSet,
                       ReviewUserViewSet,
                       TokenAPIView)


v1_router = SimpleRouter()
v1_router.register('users', ReviewUserViewSet, basename='ReviewUser')
v1_router.register('categories', CategoryViewSet, basename='Category')
v1_router.register('genres', GenreViewSet, basename='Genre')
v1_router.register('titles', TitleViewSet, basename='Title')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/token/', TokenAPIView.as_view(), name='token'),
]
