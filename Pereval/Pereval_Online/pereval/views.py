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

    def create(self, request, *args, **kwargs):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'status': status.HTTP_200_OK,
                    'message': 'Успех!',
                    'id': serializer.data['email'],
                }
            )

        if status.HTTP_400_BAD_REQUEST:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message': 'Некорректный запрос',
                    'id': None,
                }
            )

        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response(
                {
                    'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                    'message': 'Ошибка при выполнении операции',
                    'id': None,
                }
            )


class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdd.objects.all()
    serializer_class = PerevalSerializer
    filter_backends = [DjangoFilterBackend]

    # Создание объекта
    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status': status.HTTP_201_CREATED,
                 'message': 'Запись успешно создана',
                 'id': serializer.data['id']}
            )
        else:
            errors = serializer.errors
            error_status = status.HTTP_400_BAD_REQUEST if errors else status.HTTP_500_INTERNAL_SERVER_ERROR
            error_message = 'Ошибка обработки данных' if errors else 'server\'s error'
            return Response(
                {'status': error_status,
                 'message': error_message,
                 'errors': errors, 'id': None}
            )

    # Редактирование объекта в статусе 'New'
    def update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'state': '1', 'message': 'Запись успешно изменена'})
            else:
                return Response({'state': '0', 'message': serializer.errors})
        else:
            return Response({'status': '0', 'message': f'Текущий статус {pereval.status}, изменения недоступны'})


class EmailApiView(generics.ListAPIView):
    serializer_class = PerevalSerializer

    def get(self, request, *args, **kwargs):
        email = kwargs.get('email', None)
        user_exist = PerevalAdd.objects.filter(user_id__email=email)
        if user_exist:
            data = PerevalSerializer(user_exist, many=True).data
            api_status = status.HTTP_200_OK
        else:
            data = {'message': f'Нет пользователя с таким Email: {email}'}
            api_status = 404
        return JsonResponse(data, status=api_status, safe=False)
