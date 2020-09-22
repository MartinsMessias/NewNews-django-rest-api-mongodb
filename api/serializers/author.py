from rest_framework import serializers
from rest_framework.reverse import reverse

from ..models import Author


class AuthorSerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('name', 'links', )

    def get_links(self, obj):
        try:
            request = self.context['request']
            return {
                'self': reverse('author_detail', kwargs={'id': obj.pk}, request=request),
                'delete': reverse('author_detail', kwargs={'id': obj.pk}, request=request),
                'update': reverse('author_detail', kwargs={'id': obj.pk}, request=request),
            }
        except:
            pass