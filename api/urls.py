from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import routers

from .views import author as author_view, news as news_view


router = routers.DefaultRouter()


class DocsView(APIView):
    """
    New News API
    """
    def get(self, request, *args, **kwargs):
        apidocs = {
            'news': request.build_absolute_uri('news/'),
            'authors': request.build_absolute_uri('authors/')
        }
        return Response(apidocs)

router.register('news/', news_view.NewsList, basename='news')
router.register('authors/', author_view.VagaList, basename='authors')

urlpatterns = [
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('news/', news_view.NewsList.as_view(), name='news'),
    path('news/<int:id>', news_view.News.as_view(), name='news_detail'),
    path('authors/', author_view.AuthorList.as_view(), name='authors'),
    path('authors/<int:id>', author_view.Author.as_view(), name='author_detail'),
]