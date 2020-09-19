from django.contrib import admin

# Register your models here.
from api.models import News, Author

admin.site.register(Author)
admin.site.register(News)