
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer

    def get(self, request, fromat=None):
        """ Return a list of APIView features """
        an_apiview = [
            'fdsf efef rtb rerwgregrereb rbtrgrg ewrg wergr gergegwe',
            'ghter r rg bgb ewerertrrh rg rr wwe4t q 4hgthth h eer gtgerg rgreg',
            'rwe rt rhtrju ukmiyyki tey tewe rw wr5yyyh ghterq ewrg rw'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create heelo message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle partial update an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})
