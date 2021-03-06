from django.urls import path, include
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import routers

from .views import author as author_view, news as news_view


router = routers.DefaultRouter()


class APIRoot(APIView):
    """
    Cadastre autores, poste notícas e pesquise sobre algo.
    """
    def get(self, request, *args, **kwargs):
        apidocs = {
            'news': request.build_absolute_uri('news/'),
            'authors': request.build_absolute_uri('authors/'),
        }
        return Response(apidocs)

router.register('news', news_view.NewsList, basename='news')
router.register('authors', author_view.AuthorList, basename='authors')

urlpatterns = [
    path('', APIRoot.as_view()),
    path('', include(router.urls)),
    path('news/<int:id>', news_view.News.as_view(), name='news_detail'),
    path('authors/<int:id>', author_view.Author.as_view(), name='author_detail'),
]