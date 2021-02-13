from aiogram import types

PAYMENTS_PROVIDER_TOKEN = '381764678:TEST:20650'
TOKEN = '1322316063:AAFjg5Fl1V3_zuRvRIIFeZI_eWqXGDDGNz4'  # заменить на токен своего бота
TIMEZONE = 'Europe/MSK'
TIMEZONE_COMMON_NAME = 'Moscow'
PRICE = types.LabeledPrice(label='Подготовка пакета документов', amount=42000)
COPS_URL = 'https://c.beznen.ru/wp-content/uploads/2018/11/politsiya.jpg'
ZHKH_URL = 'https://www.люберцы.рф/sites/default/files/s1200_0.png'

images = {
    'Полиция': COPS_URL,
    'ЖКХ': ZHKH_URL
}

