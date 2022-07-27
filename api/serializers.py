from rest_framework import serializers

from .models import Url


class UrlSerializers(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = '__all__'


class UrlReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('main_url', 'lifetime', 'time_url')
