from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from ..models import Author
from ..serializers import author as author_serializer
from ..services import author as author_service
from ..entities import author as author_entitie

class AuthorList(GenericAPIView):

    serializer_class = author_serializer.AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, format=None):
        """Listar autores"""
        authors = author_service.list_authors()
        serializer = author_serializer.AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """Cadastrar autor"""
        serializer = author_serializer.AuthorSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data["name"]
            new_author = author_entitie.Author(name=name)
            author_service.create_author(new_author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Author(GenericAPIView):

    serializer_class = author_serializer.AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, id, format=None):
        """Retorna o autor pelo id"""
        author = author_service.get_author(id)
        serializer = author_serializer.AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        """Editar dados de autor"""
        author = author_service.get_author(id)
        serializer = author_serializer.AuthorSerializer(author, data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            new_author = author_entitie.Author(name=name)
            author_service.edit_author(author, new_author)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """ Deletar autor por id"""
        author = author_service.get_author(id)
        author_service.delete_author(author)
        return Response(status=status.HTTP_204_NO_CONTENT)