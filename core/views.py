
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'All other Rest APIs Goes Here'}
        return Response(content)

    def post(self, request):
        dummy_var = request.data.get('dummy_var')
        content = {'message': 'You Just Created a Post Content {}'.format(dummy_var)}
        return Response(content)


class UserManagement(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'All User Management Code Goes Here'}
        return Response(content)


class VisitorManagement(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'All Visitor Management Code Goes Here'}
        return Response(content)


class DeliveryManagement(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'All Delivery Management Code Goes Here'}
        return Response(content)
