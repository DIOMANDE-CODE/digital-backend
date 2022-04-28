from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .models import Emailing
from .serializers import EmailingSerializer
from django.core.mail import BadHeaderError, EmailMessage
# Create your views here.

class EmailingList(APIView):
    def get(self, request, format=None):
        contact = Emailing.objects.all()
        serializer = EmailingSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmailingSerializer(data=request.data)
        if serializer.is_valid():
            # send_mail = EmailMessage(
            #     serializer.data['sujet'],
            #     serializer.data['message'],
            #     serializer.data['mail'],
            #     [settings.EMAIL_HOST_USER],
            #     reply_to= (serializer.data['mail'],)
            # )
            # send_mail.send()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)