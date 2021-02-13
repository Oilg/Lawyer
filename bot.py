import asyncio

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

import config
from messages import MESSAGES
from problems.search_mapping import serialized_mapping, process_search, MAPPING, all_subtypes, all_subtypes_regex

loop = asyncio.get_event_loop()
bot = Bot(config.TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot, loop=loop)

PRICE = types.LabeledPrice(label='Кек', amount=42000)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    kb_layout = ReplyKeyboardMarkup()
    for type in MAPPING:
        kb_layout.add(KeyboardButton(type))
    await message.reply("Привет\!\n"
                        "Что случилось?\n"
                        "Напишите текстом или используйте кнопки ниже",
                        reply_markup=kb_layout)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler(commands=['buy'])
async def process_buy_command(message: types.Message):
    if config.PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, MESSAGES['pre_buy_demo_alert'])
        await bot.send_invoice(
            message.chat.id,
            title=MESSAGES['tm_title'],
            description=MESSAGES['tm_description'],
            provider_token=config.PAYMENTS_PROVIDER_TOKEN,
            currency='rub',
            photo_url=config.images[message.text],
            photo_height=512,  # !=0/None, иначе изображение не покажется
            photo_width=512,
            photo_size=512,
            is_flexible=False,  # True если конечная цена зависит от способа доставки
            prices=[PRICE],
            start_parameter='time-machine-example',
            payload='some\-invoice\-payload\-for\-our\-internal\-use'
        )


@dp.message_handler(regexp='ЖКХ|ФССП')
async def get_subtypes(msg: types.Message):
    reply_markup = ReplyKeyboardMarkup(one_time_keyboard=True)
    for types in MAPPING[msg.text]:
        reply_markup.add(KeyboardButton(types.name))
    await msg.reply("Выберите ситуацию", reply_markup=reply_markup)


@dp.message_handler(regexp=all_subtypes_regex)
async def kek(msg: types.Message):
    await msg.reply('Нашли\! Готовы заполнять?')


@dp.message_handler()
async def search(msg: types.Message):
    await msg.reply('По вашему поиску мы нашли следующие ситуации:\nдля возврата используйте команду /start',
                    reply_markup=process_search(msg.text))


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency
        )
    )


if __name__ == '__main__':
    executor.start_polling(dp)
