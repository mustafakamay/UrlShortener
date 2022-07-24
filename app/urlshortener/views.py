from rest_framework.views import APIView
from .serializers import UrlShortenerListSerializer, UrlShortenerSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import UrlShortener
from rest_framework import generics
from .helpers import generate_short_url
from app.settings import HOST
from django.shortcuts import redirect

class CreateShortUrlView(APIView):


    def post(self,request,*args, **kwargs):

        serializer = UrlShortenerSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        short_path= generate_short_url()
        short_url = '{}{}'.format(HOST,short_path)

        UrlShortener.objects.create(originUrl=serializer.data['originUrl'],
            shortUrl=short_path)

        data = {
            "Origin_Url":serializer.data['originUrl'],
            "Short_Url":short_url
        }
        return Response(status=status.HTTP_201_CREATED,data=data)

class ListAllUrlView(generics.ListAPIView):

    serializer_class = UrlShortenerListSerializer
    queryset = UrlShortener.objects.all()


def redirectUrl(request, shorturl):
    instance = UrlShortener.objects.filter(shortUrl=shorturl).first()
    instance.visit += 1
    instance.save()
    return redirect(instance.originUrl)