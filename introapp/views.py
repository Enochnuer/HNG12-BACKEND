from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.conf import settings
from datetime import datetime
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def display_info(request):
    

    current_time_in_utc = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

    data = {
        "email": settings.EMAIL_ADDRESS,
        "current_datetime": current_time_in_utc,
        "github_url": settings.GITHUB_URL

    }

    return Response(data=data, status=status.HTTP_200_OK)


    