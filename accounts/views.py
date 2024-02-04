from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from face_ai import main_Copy
from .models import *
from .serializer import *


# Create your views here
class HelloView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class ImageUploadView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = ImageModelSerializer(data=request.data)
        d=request.data
        d_name=d['name']
        d_id=d['account_id']
        d_img=d['image']
        print(d_img)
        rf_img = d_img
        if serializer.is_valid():
            # Customize the image file name before saving
            image_instance = serializer.validated_data['image']
            image_instance.name = self.modify_image_name(d_name,d_id)
            serializer.save()
            print(serializer.data)
            b=serializer.data
            face_detection=main_Copy.f_a(b['image'])
            data={
            "name":b['name'],
            "iamge":b['image'],
            "name":b['name'],
            "face_detection":face_detection
            }
            return Response(data, status=status.HTTP_201_CREATED)
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def modify_image_name(self, name,id):
        # Implement your logic to modify the image name here
        # For example, you can add a timestamp or use a unique identifier
        modified_name = id+name+".png"
        return modified_name