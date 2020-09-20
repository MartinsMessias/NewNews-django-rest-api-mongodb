from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..models import News
from ..serializers import news as news_serializer
from ..services import news as news_service
from ..entities import news as news_entitie

class NewsList(GenericAPIView):

    serializer_class = news_serializer.NewsSerializer
    queryset = News.objects.all()

    def get(self, request, format=None):
        """Listar Notícias"""
        news = news_service.list_news()
        serializer = news_serializer.NewsSerializer(news, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

    @classmethod
    def get_extra_actions(cls):
        return []

class News(GenericAPIView):

    serializer_class = news_serializer.NewsSerializer
    queryset = News.objects.all()

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