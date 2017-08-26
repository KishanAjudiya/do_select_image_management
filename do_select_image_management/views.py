import os
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from do_select_image_management.settings import MEDIA_ROOT


class Images(APIView):
    """

    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return render(request, "manage_images.html")


class ManageImage(APIView):
    permission_classes = (IsAuthenticated,)

    """
    :param
        
    """
    def get(self, request):
        image_name = request.GET.get('image_name', '')
        if image_name:
            file = open(MEDIA_ROOT + image_name, "r")
            if file:
                return Response(file.read(), status=None, template_name=None, headers=None, content_type=None)
        return Response({"msg": "No Image found"}, status=None, template_name=None, headers=None, content_type=None)

    def post(self, request):
        image_data = request.data.get('image_data', '')
        image_name = request.data.get('image_name', '')
        if image_data and image_name:
            file = open(MEDIA_ROOT + image_name, "w")
            file.write(image_data)
            file.close()
            return Response({"msg": "Image Saved Successfully."}, status=None, template_name=None, headers=None, content_type=None)
        return Response({}, status=None, template_name=None, headers=None, content_type=None)

    def put(self, request):
        image_data = request.data.get('image_data', '')
        image_name = request.data.get('image_name', '')
        if image_data and image_name:
            file = open(MEDIA_ROOT + image_name, "w")
            file.write(image_data)
            file.close()
            return Response({"msg": "Image Saved Successfully."}, status=None, template_name=None, headers=None, content_type=None)
        return Response({}, status=None, template_name=None, headers=None, content_type=None)

    def delete(self, request):
        image_name = request.data.get('image_name', '')
        file = open(MEDIA_ROOT + image_name, "r")
        if file:
            file.close()
            os.remove(MEDIA_ROOT + image_name)
        return Response({"msg": "Image deleted Successfully."}, status=None, template_name=None, headers=None, content_type=None)


class ImageList(APIView):
    """
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        result = {}
        for files in os.listdir(MEDIA_ROOT):
            file = open(MEDIA_ROOT + files, "r")
            result[files] = file.read()
            file.close()
        if result:
            return Response(result, status=None, template_name=None, headers=None, content_type=None)
        return Response({"msg": "No Image found"}, status=500, template_name=None, headers=None, content_type=None)