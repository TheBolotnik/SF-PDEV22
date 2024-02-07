from django.http import JsonResponse
from rest_framework import viewsets
from pereval.serializers import *
from .models import PerevalAdd, Coord, Level, Users, Images
from rest_framework.response import Response
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [DjangoFilterBackend]

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'message': 'Success', 'id': serializer.data['id']})
        else:
            errors = serializer.errors
            error_status = status.HTTP_400_BAD_REQUEST if errors else status.HTTP_500_INTERNAL_SERVER_ERROR
            error_message = 'failed to process the data' if errors else 'server\'s error'
            return Response({'status': error_status, 'message': error_message, 'errors': errors, 'id': None})

    def update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)#partial= True enables partial update
            if serializer.is_valid():
                serializer.save()
                return Response({'state': '1', 'message': 'successfully updated'})
            else:
                return Response({'state': '0', 'message': serializer.errors})
        else:
            return Response({'status': '0', 'message': f'current status is {pereval.status}, changes aren\'t allowed'})


class EmailApiView(generics.ListAPIView):
    serializer_class = PerevalSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        user_exist = PerevalAdd.objects.filter(user_id__email=email)
        if user_exist:
            data = PerevalSerializer(user_exist, many=True).data
        else:
            data = {'message': f'there is no user with email: {email}'}
        return JsonResponse(data, safe=False)
