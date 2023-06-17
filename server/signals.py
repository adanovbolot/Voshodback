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

            if response.status_code == 201 or response.status_code == 200:
                try:
                    response_json = response.json()
                    logger.info(response_json)
                except ValueError:
                    logger.warning('Некорректный формат JSON-ответа')
            else:
                logger.error(f'Ошибка при отправке данных в Evotor. Код ошибки: {response.status_code}')

            if response.status_code == 201 or response.status_code == 200:
                logger.info('Данные успешно отправлены в Evotor')
            else:
                logger.error(f'Ошибка при отправке данных в Evotor. Код ошибки: {response.status_code}')


@receiver(post_save, sender=models.Product)
def send_all_records(sender, instance=None, created=False, **kwargs):
    if created:
        url = 'https://api.evotor.ru/api/v1/inventories/stores/20200829-EF34-40C6-803A-06A5F50BB714/products'
        all_records = models.Product.objects.all()
        serialized_records = serializers.ProductSerializer(all_records, many=True).data

        token = get_evotor_token()
        if not token:
            print('Token not found.')
            return

        headers = {
            'X-Authorization': token,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=serialized_records, headers=headers)

        if response.status_code == 201:
            print('All records sent successfully.')
        else:
            print(f'Failed to send all records. Status code: {response.status_code}')


def get_evotor_token():
    evotor_token = models.EvotorToken.objects.first()
    if not evotor_token:
        return None
    return evotor_token.token
