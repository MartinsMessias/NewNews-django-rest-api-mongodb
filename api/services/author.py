from django.http import Http404

from ..models import Author

# Cadastrar autor
def create_author(author):
    return Author.objects.create(name=author.name)

# Listar todos os autores
def list_authors():
    authors = Author.objects.all()
    return authors

# Listar autor pelo id
def get_author(id):
    try:
        return Author.objects.get(id=id)
    except Author.DoesNotExist:
        raise Http404

# Editar autor
def edit_author(author_data, new_author_data):
    author_data.name = new_author_data.name
    author_data.save(force_update=True)

# Remover autor
def delete_author(author):
    author.delete()

