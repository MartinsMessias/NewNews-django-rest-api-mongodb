from rest_framework import serializers
from rest_framework.reverse import reverse

from ..models import News


class NewsSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    author_name = serializers.CharField(source='author.name', read_only=True)

    class Meta:
        model = News
        fields = ('title', 'content', 'author', 'author_name', 'links', )

    def get_links(self, obj):
        try:
            request = self.context['request']
            return {
                'self': reverse('news_detail', kwargs={'id': obj.pk}, request=request),
                'delete': reverse('news_detail', kwargs={'id': obj.pk}, request=request),
                'update': reverse('news_detail', kwargs={'id': obj.pk}, request=request),
            }
        except:
            pass