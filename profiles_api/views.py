
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """
    def get(self, request, fromat=None):
        """ Return a list of APIView features """
        an_apiview = [
            'fdsf efef rtb rerwgregrereb rbtrgrg ewrg wergr gergegwe',
            'ghter r rg bgb ewerertrrh rg rr wwe4t q 4hgthth h eer gtgerg rgreg',
            'rwe rt rhtrju ukmiyyki tey tewe rw wr5yyyh ghterq ewrg rw'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
