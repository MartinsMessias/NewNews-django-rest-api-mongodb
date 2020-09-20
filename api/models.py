from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

