from typing_extensions import Required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIview

from profiles_api import serializers


class HelloApiView(APIview):

    serializer_class = serializers.HelloSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )