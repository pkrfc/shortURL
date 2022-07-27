from .models import Url
from rest_framework import serializers


class UrlSerializers(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = '__all__'


class UrlReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('main_url', 'lifetime', 'time_url')






