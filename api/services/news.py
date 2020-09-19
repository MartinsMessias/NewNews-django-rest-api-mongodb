from django.http import Http404

from ..models import News

# Cadastrar notícia
def create_news(news):
    return News.objects.create(title=news.title, content=news.content, author=news.author)

# Listar todos as notícias
def list_news():
    news = News.objects.all()
    return news


# Listar notícia pelo id
def get_news(id):
    try:
        return News.objects.get(id=id)
    except News.DoesNotExist:
        raise Http404

# Editar notícia
def edit_news(news_data, new_news_data):
    news_data.title = new_news_data.title
    news_data.content = new_news_data.content
    news_data.author = new_news_data.author
    news_data.save(force_update=True)


# Remover notícia
def delete_news(news):
    news.delete()

