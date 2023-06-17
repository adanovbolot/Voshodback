import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from . import models
from . import serializers


logger = logging.getLogger(__name__)


@receiver(post_save, sender=models.Product)
def send_to_evotor(sender, **kwargs):
    def get_evotor_token():
        evotor_token = models.EvotorToken.objects.first()
        if not evotor_token:
            return None
        return evotor_token.token

    url = 'https://api.evotor.ru/api/v1/inventories/stores/20200829-EF34-40C6-803A-06A5F50BB714/products'
    token = get_evotor_token()

    if token:
        headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        }
        products = models.Product.objects.all()

        for product in products:
            serialized_data = serializers.ProductSerializer(product).data

            if product.id is not None:
                product_url = f'{url}/{product.id}'
                response = requests.put(product_url, json=serialized_data, headers=headers)
            else:
                response = requests.post(url, json=serialized_data, headers=headers)

            logger.info('Данные для Evotor:')
            logger.info(serialized_data)
            logger.info('Ответ от Evotor:')
            logger.info(response.json())

            if response.status_code == 201 or response.status_code == 200:
                logger.info('Данные успешно отправлены в Evotor')
            else:
                logger.error(f'Ошибка при отправке данных в Evotor. Код ошибки: {response.status_code}')

