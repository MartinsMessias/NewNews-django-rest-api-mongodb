from rest_framework import status, filters, mixins, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..models import News as model_news
from ..pagination import CustomPagination
from ..serializers import news as news_serializer
from ..services import news as news_service
from ..entities import news as news_entitie

class NewsList(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = news_serializer.NewsSerializer
    queryset = model_news.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'author__name']

    def get(self, request, format=None):
        """Listar Notícias"""
        pagination = CustomPagination()
        news = news_service.list_news()
        results = pagination.paginate_queryset(news, request)
        serializer = news_serializer.NewsSerializer(results, context={'request': request}, many=True)
        return pagination.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        """Cadastrar notícia"""
        serializer = news_serializer.NewsSerializer(data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data["title"]
            content = serializer.validated_data["content"]
            author = serializer.validated_data["author"]
            new_news = news_entitie.News(title=title, content=content, author=author)
            news_service.create_news(new_news)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class News(GenericAPIView):

    serializer_class = news_serializer.NewsSerializer
    queryset = model_news.objects.all()

    def get(self, request, id, format=None):
        """Retorna a notícia pelo id"""
        news = news_service.get_news(id)
        serializer = news_serializer.NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        """Editar dados da noticia"""
        news = news_service.get_news(id)
        serializer = news_serializer.NewsSerializer(news, data=request.data)

        if serializer.is_valid():
            title = serializer.validated_data["title"]
            content = serializer.validated_data["content"]
            author = serializer.validated_data["author"]
            new_news = news_entitie.News(title=title, content=content, author=author)
            news_service.edit_news(news, new_news)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        """ Deletar noticia por id"""
        news = news_service.get_news(id)
        news_service.delete_news(news)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @classmethod
    def get_extra_actions(cls):
        return []
