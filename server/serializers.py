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
