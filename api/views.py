import time

from django.views.generic import RedirectView
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .models import Url
from .serializers import UrlSerializers, UrlReadSerializers


@api_view(['POST'])
def short(request):
    main_url = request.data.get('main_url')
    lifetime = request.data.get('lifetime')
    short_url = int(time.time())
    short_url_view = 'http://127.0.0.1:8000/api/short-you-url/' + str(short_url)
    data = {'main_url': main_url, 'short_url': short_url, 'short_url_view': short_url_view, 'lifetime': lifetime}
    serializer = UrlSerializers(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShortView(APIView):
    def get(self, request, url):
        urls = Url.objects.filter(short_url=url)
        serializer = UrlReadSerializers(urls, many=True)
        return Response(serializer.data)
