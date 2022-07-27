import time
from datetime import datetime, timedelta

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Url
from .serializers import UrlReadSerializers, UrlSerializers


@api_view(['POST'])
def short(request):
    main_url = request.data.get('main_url')
    lifetime = request.data.get('lifetime')
    short_url = int(time.time())
    short_url_view = 'http://127.0.0.1:8000/api/short-you-url/' + str(
        short_url
    )
    data = {
        'main_url': main_url,
        'short_url': short_url,
        'short_url_view': short_url_view,
        'lifetime': lifetime
    }
    serializer = UrlSerializers(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShortView(APIView):
    def get(self, request, url):
        urls = Url.objects.filter(short_url=url)
        serializer = UrlReadSerializers(urls, many=True)
        lifetime = timedelta(urls.values('lifetime').get().get('lifetime'))
        time_url = urls.values('time_url').get().get('time_url')
        now = datetime.now().date()
        if lifetime + time_url > now:
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
