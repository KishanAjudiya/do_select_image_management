import os
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from do_select_image_management.settings import MEDIA_ROOT


class Images(APIView):
    """
    This view is used for rendering the html page
    contains the image management functionality.
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        return render(request, "manage_images.html")


class ManageImage(APIView):
    permission_classes = (IsAuthenticated,)

    """
    This view is used for managing images.    
    """
    def get(self, request):
        """
        Method to get particular one image.
        :param request: image_name
        :return: {"image_name":"image_data"}
        """
        image_name = request.GET.get('image_name', '')
        if image_name:
            file = open(MEDIA_ROOT + image_name, "r")
            if file:
                return Response(file.read(), status=None, template_name=None, headers=None, content_type=None)
        return Response({"msg": "No Image found"}, status=None, template_name=None, headers=None, content_type=None)

    def post(self, request):
        """
        Method to save new image
        :param request: image_data ( base64 format ), image_name
        :return: {'msg':""}
        """
        image_data = request.data.get('image_data', '')
        image_name = request.data.get('image_name', '')
        if image_data and image_name:
            file = open(MEDIA_ROOT + image_name, "w")
            file.write(image_data)
            file.close()
            return Response({"msg": "Image Saved Successfully."}, status=None, template_name=None, headers=None, content_type=None)
        return Response({}, status=None, template_name=None, headers=None, content_type=None)

    def put(self, request):
        """
        Method to update image.
        :param request: image_name, image_data ( base64 format )
        :return: {'msg':""}
        """
        image_data = request.data.get('image_data', '')
        image_name = request.data.get('image_name', '')
        if image_data and image_name:
            file = open(MEDIA_ROOT + image_name, "w")
            file.write(image_data)
            file.close()
            return Response({"msg": "Image Saved Successfully."}, status=None, template_name=None, headers=None, content_type=None)
        return Response({}, status=None, template_name=None, headers=None, content_type=None)

    def delete(self, request):
        """
        Method to delete one particular image
        :param request: image_name
        :return: {'msg':""}
        """
        image_name = request.data.get('image_name', '')
        file = open(MEDIA_ROOT + image_name, "r")
        if file:
            file.close()
            os.remove(MEDIA_ROOT + image_name)
        return Response({"msg": "Image deleted Successfully."}, status=None, template_name=None, headers=None, content_type=None)


class ImageList(APIView):
    """
    This view is used for getting all the saved images.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Method to get all the images data.
        :param request:
        :return: {"image_name_1":"image_data_1", "image_name_2":"image_data_2"....}
        """
        result = {}
        for files in os.listdir(MEDIA_ROOT):
            file = open(MEDIA_ROOT + files, "r")
            result[files] = file.read()
            file.close()
        if result:
            return Response(result, status=None, template_name=None, headers=None, content_type=None)
        return Response({"msg": "No Image found"}, status=500, template_name=None, headers=None, content_type=None)