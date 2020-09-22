# NewNews API
##### Cadastre autores, poste notícas e pesquise sobre algo.

<div align="center">

[![GitHub stars](https://img.shields.io/github/stars/MartinsMessias/NewNews-django-rest-api)](https://github.com/MartinsMessias/NewNews-django-rest-api)<space> <space>[![GitHub license](https://img.shields.io/github/license/MartinsMessias/NewNews-django-rest-api)](https://github.com/MartinsMessias/NewNews-django-rest-api/blob/master/LICENSE)<space> <space>[![GitHub forks](https://img.shields.io/github/forks/MartinsMessias/NewNews-django-rest-api)](https://github.com/MartinsMessias/NewNews-django-rest-api/)

</div>
---

## 📖 Sobre:

Uma api onde é possível cadastrar autores e notícias, também é possível realizar pesquisa por notícias.

--- 

## 🚀 Tecnologias Utilizadas:

- Python
- Django
- Django Rest Framework
- MongoDB Atlas
- Djongo
- Heroku
--- 

#### Documentação no Postman
[Documentação](https://documenter.getpostman.com/view/12776670/TVKD2xL3)

[Testar online](https://api-newnews.herokuapp.com/)
##### *Aguardar o tempo de carregamento do Heroku.*

### Documentação básica

```

Listar autores
GET https://api-newnews.herokuapp.com/authors/
```
---------------------------------------------
```
Cadastrar autor
POST https://api-newnews.herokuapp.com/authors/

BODY raw

{
    "name":"Autor Lima"
}

```
---------------------------------------------
```
Listar notícias
GET https://api-newnews.herokuapp.com/news/
```
---------------------------------------------
```
Cadastrar notícias
POST https://api-newnews.herokuapp.com/news/

BODY raw

{
    "title": "Título da notícia",
    "content": "Conteúdo da notícia",
    "author": 4
}

```
---------------------------------------------
```
Pesquisar notícias
Traz notícias que contenham a query de busca no seu titulo, conteúdo ou nome do autor.

GET https://api-newnews.herokuapp.com/news/?search=Silva

PARAMS
search | Silva
```
