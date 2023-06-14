from rest_framework import serializers
from . import models
from .models import TerminalUser


class EvotorUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EvotorUsers
        fields = ('id', 'userId', 'token')


class EvotorTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EvotorToken
        fields = '__all__'


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shops
        fields = '__all__'


class EvotorOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EvotorOperator
        fields = ['uuid', 'name', 'code', 'stores', 'role']


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Terminal
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Receipt
        fields = "__all__"


class TerminalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerminalUser
        fields = '__all__'

    def to_internal_value(self, data):
        uuid = data.get('uuid')
        name = data.get('name')
        lastName = data.get('lastName')
        patronymicName = data.get('patronymicName')
        phone = data.get('phone')
        code = data.get('code')
        stores = data.get('stores', [])
        role = data.get('role')

        return {
            'uuid': uuid,
            'name': name,
            'lastName': lastName,
            'patronymicName': patronymicName,
            'phone': phone,
            'code': code,
            'stores': stores,
            'role': role
        }


class TerminalKassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Terminal
        fields = '__all__'

    def to_internal_value(self, data):
        uuid = data.get('uuid')
        name = data.get('name')
        store_uuid = data.get('store_uuid')
        timezone_offset = data.get('timezone_offset')

        return {
            'uuid': uuid,
            'name': name,
            'store_uuid': store_uuid,
            'timezone_offset': timezone_offset
        }
