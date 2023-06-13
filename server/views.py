from rest_framework.response import Response

from .serializers import ReceiptSerializer
from .utils import generate_token
import logging
import requests
from rest_framework import generics
from . import models
from rest_framework import status
from . import serializers
from rest_framework.views import APIView


logger = logging.getLogger(__name__)


class EvotorUsersCreate(generics.ListCreateAPIView):
    queryset = models.EvotorUsers.objects.all()
    serializer_class = serializers.EvotorUsersSerializer

    def perform_create(self, serializer):
        token = generate_token()
        userId = self.request.data.get('userId')
        serializer.save(token=token, userId=userId)
        logger = logging.getLogger(__name__)
        logger.info(f"Token '{token}' сохранен в базе данных.")
        logger.info(f"Request data: {self.request.data}")
        logger.info(f"Serializer data: {serializer.data}")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_data = {
            'token': serializer.data['token'],
            'userId': serializer.data['userId']
        }
        logger = logging.getLogger(__name__)
        logger.info(f"Response data: {response_data}")
        return Response(response_data, status=status.HTTP_200_OK, headers=headers)


class EvotorUsersDelete(APIView):
    def post(self, request):
        if request.data.get('type') != 'ApplicationUninstalled':
            return Response({'ошибка': 'Неверный тип запроса'}, status=status.HTTP_400_BAD_REQUEST)
        userId = request.data.get('data', {}).get('userId')
        if not userId:
            return Response({'ошибка': 'Отсутствует идентификатор пользователя (userId)'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = models.EvotorUsers.objects.filter(userId=userId).first()
            token = models.EvotorToken.objects.filter(userId=userId).first()
            if user:
                user.delete()
                logger.info(f"Объект EvotorUsers с userId '{userId}' удален.")
            if token:
                token.delete()
                logger.info(f"Объект EvotorToken с userId '{userId}' удален.")
            if user or token:
                return Response({'сообщение': 'Объекты удалены'}, status=status.HTTP_200_OK)
            else:
                logger.info(f"Объекты с userId '{userId}' не найдены.")
                return Response({'ошибка': 'Объекты не найдены'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Ошибка при удалении объектов: {str(e)}")
            return Response({'ошибка': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EvotorUsersAuth(APIView):
    def post(self, request):
        userId = request.data.get('userId')

        if not userId:
            return Response({'ошибка': 'Отсутствует идентификатор пользователя (userId)'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            user = models.EvotorUsers.objects.get(userId=userId)
            token = user.token
            logger.info(f"Авторизация пользователя с userId '{userId}' успешна.")
            return Response({'userId': userId, 'token': token}, status=status.HTTP_200_OK)
        except models.EvotorUsers.DoesNotExist:
            logger.info(f"Пользователь с userId '{userId}' не найден.")
            return Response({'ошибка': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Ошибка при авторизации пользователя: {str(e)}")
            return Response({'ошибка': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EvotorGetToken(APIView):
    def post(self, request, format=None):
        serializer = serializers.EvotorTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            logger.info('Пользователь успешно создан.',
                        extra={'request': request, 'user_id': user.id, 'token': user.token})
            response_data = {
                'status': 'success',
                'message': 'Пользователь успешно создан.',
                'user_id': user.id,
                'token': user.token,
                'additional_data': 'Дополнительные данные'
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            errors = serializer.errors
            for field, error in errors.items():
                logger.warning(f'Ошибка валидации поля {field}: {error}',
                               extra={'request': request, 'validation_error': f'{field}: {error}'})
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class EvotorTokenCreate(generics.CreateAPIView):
    queryset = models.EvotorToken.objects.all()
    serializer_class = serializers.EvotorTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        logger.info('Токен успешно создан.',
                    extra={'request': request, 'token_data': serializer.data})

        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

        logger.info('Токен сохранен в базе данных.')


class EvotorTokenDelete(APIView):
    def post(self, request):
        if request.data.get('type') != 'ApplicationUninstalled':
            return Response({'ошибка': 'Неверный тип запроса'}, status=status.HTTP_400_BAD_REQUEST)
        userId = request.data.get('data', {}).get('userId')
        if not userId:
            return Response({'ошибка': 'Отсутствует идентификатор пользователя (userId)'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            token = models.EvotorToken.objects.filter(userId=userId).first()
            if token:
                token.delete()
                logger.info(f"Запись с userId '{userId}' удалена.")
                return Response({'сообщение': 'Запись удалена'}, status=status.HTTP_200_OK)
            else:
                logger.info(f"Запись с userId '{userId}' не найдена.")
                return Response({'ошибка': 'Запись не найдена'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Ошибка при удалении записи: {str(e)}")
            return Response({'ошибка': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ShopsCreateOrUpdateView(generics.ListCreateAPIView):
    queryset = models.Shops.objects.all()
    serializer_class = serializers.ShopsSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        logger.info(f'Создан новый объект Магазин: {instance}')

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if name:
            instance, created = models.Shops.objects.get_or_create(name=name)
            if not created:
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)
                logger.info(f'Обновлен объект Магазин: {instance}')
                return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(f'Создан новый объект Магазин: {serializer.data}')
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_update(self, serializer):
        instance = serializer.save()
        logger.info(f'Обновлен объект Магазин: {instance}')

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EvotorOperatorView(APIView):
    def get(self, request):
        evotor_token = models.EvotorToken.objects.first()
        if not evotor_token:
            return Response('Токен не найден', status=status.HTTP_400_BAD_REQUEST)
        token = evotor_token.token
        url = 'https://api.evotor.ru/api/v1/inventories/employees/search'
        headers = {
            'X-Authorization': token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()

            for item in json_data:
                uuid = item['uuid']
                name = item['name']
                code = item['code']
                stores = item['stores'][0] if item['stores'] else None
                role = item['role']

                evotor_operator, created = models.EvotorOperator.objects.get_or_create(uuid=uuid)
                if not created:
                    evotor_operator.name = name
                    evotor_operator.code = code
                    evotor_operator.stores = stores
                    evotor_operator.role = role

                evotor_operator.save()

            serializer = serializers.EvotorOperatorSerializer(models.EvotorOperator.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ShopsView(APIView):
    def get(self, request):
        evotor_token = models.EvotorToken.objects.first()
        if not evotor_token:
            return Response('Токен не найден', status=status.HTTP_400_BAD_REQUEST)
        token = evotor_token.token
        url = 'https://api.evotor.ru/api/v1/inventories/stores/search'
        headers = {
            'X-Authorization': token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            for item in json_data:
                uuid = item['uuid']
                address = item['address']
                name = item['name']
                code = item['code']

                shop, created = models.Shops.objects.get_or_create(uuid=uuid)
                if not created:
                    shop.address = address
                    shop.name = name
                    shop.code = code

                shop.save()
            serializer = serializers.ShopsSerializer(models.Shops.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TerminalView(APIView):
    def get(self, request):
        evotor_token = models.EvotorToken.objects.first()
        if not evotor_token:
            return Response('Токен не найден', status=status.HTTP_400_BAD_REQUEST)
        token = evotor_token.token
        url = 'https://api.evotor.ru/api/v1/inventories/devices/search'
        headers = {
            'X-Authorization': token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()

            terminals = []
            for item in json_data:
                uuid = item['uuid']
                name = item['name']
                store_uuid = item['storeUuid']
                timezone_offset = item['timezoneOffset']

                terminal, created = models.Terminal.objects.get_or_create(uuid=uuid)
                terminal.name = name
                terminal.store_uuid = store_uuid
                terminal.timezone_offset = timezone_offset
                terminal.save()
                terminals.append(terminal)

            serializer = serializers.TerminalSerializer(terminals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = serializers.TerminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get_evotor_token(self):
        evotor_token = models.EvotorToken.objects.first()
        if not evotor_token:
            return None
        return evotor_token.token

    def get(self, request):
        token = self.get_evotor_token()
        if not token:
            return Response('Токен не найден', status=status.HTTP_400_BAD_REQUEST)

        url = 'https://api.evotor.ru/api/v1/inventories/stores/20200829-EF34-40C6-803A-06A5F50BB714/products'
        headers = {
            'X-Authorization': token
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()

            for item in json_data:
                uuid = item['uuid']
                product, _ = models.Product.objects.update_or_create(uuid=uuid, defaults=item)
            serializer = serializers.ProductSerializer(models.Product.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ProductCreate(APIView):
    def get_evotor_token(self):
        evotor_token = models.EvotorToken.objects.first()
        if not evotor_token:
            return None
        return evotor_token.token

    def post(self, request):
        token = self.get_evotor_token()
        if not token:
            return Response('Токен не найден', status=status.HTTP_400_BAD_REQUEST)

        url = 'https://api.evotor.ru/api/v1/inventories/stores/20200829-EF34-40C6-803A-06A5F50BB714/products'
        headers = {
            'X-Authorization': token,
            'Content-Type': 'application/json'
        }
        data = request.data
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            json_data = response.json()
            uuid = json_data['uuid']
            product, _ = models.Product.objects.update_or_create(uuid=uuid, defaults=json_data)
            serializer = serializers.ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ReceiptView(APIView):
    def post(self, request):
        data = request.data

        receipt_data = {
            "id_receipt": data.get("id"),
            "timestamp": data.get("timestamp"),
            "userId": data.get("userId"),
            "type": data.get("type"),
            "version": data.get("version"),
            "deviceId": data.get("data").get("deviceId"),
            "storeId": data.get("data").get("storeId"),
            "dateTime": data.get("data").get("dateTime"),
            "shiftId": data.get("data").get("shiftId"),
            "employeeId": data.get("data").get("employeeId"),
            "paymentSource": data.get("data").get("paymentSource"),
            "infoCheck": data.get("data").get("infoCheck"),
            "egais": data.get("data").get("egais"),
            "totalTax": data.get("data").get("totalTax"),
            "totalDiscount": data.get("data").get("totalDiscount"),
            "totalAmount": data.get("data").get("totalAmount"),
            "extras": data.get("data").get("extras"),
        }

        serializer = ReceiptSerializer(data=receipt_data)
        if serializer.is_valid():
            receipt = serializer.save()
            serialized_data = ReceiptSerializer(receipt).data
            logger.info("Данные успешно сохранены: %s", serialized_data)
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        logger.error(f"Ошибка валидации данных: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TerminalUserView(generics.UpdateAPIView):
    queryset = models.TerminalUser.objects.all()
    serializer_class = serializers.TerminalUserSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            uuid = serializer.validated_data['uuid']
            terminal_user, created = models.TerminalUser.objects.get_or_create(uuid=uuid)
            serializer.instance = terminal_user
            self.perform_update(serializer)
            serialized_data = serializer.data
            logger.info("Данные успешно сохранены: %s", serialized_data)
            print("Данные успешно сохранены:", serialized_data)
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            logger.error("Ошибка валидации данных: %s", serializer.errors)
            print("Ошибка валидации данных:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
