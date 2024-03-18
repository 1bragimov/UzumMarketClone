import aiogram
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, BotCommand
from root import TOKEN


dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer_photo(photo="https://images.app.goo.gl/BzpMtZdoGCiPusTT6",
                               caption=f"Assalomu alaykum {message.from_user.full_name} Bizning 🏪 Uzum Market botimizga xush kelibsiz 👋")


@dp.message(F.text == "Iphone")
async def telefonlar(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/clrb7ops99oopol1gl60/original.jpg",
                               caption="Apple iPhone 15 Pro"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 128gb"
                                       "\nPhone price💸: 18 869 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-apple-iphone-15-pro-857375?skuid=2339768")
    await message.answer_photo(photo="https://images.uzum.uz/clrb7ops99oopol1gl60/original.jpg",
                               caption="Apple Iphone 15 pro"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 256gb"
                                       "\nPhone price💸: 20 723 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-apple-iphone-15-pro-857375?skuid=2339769")
    await message.answer_photo(photo="https://images.uzum.uz/cmus4m925kub33f26ar0/original.jpg",
                               caption="Apple Iphone 14 pro max"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 128gb"
                                       "\nPhone price💸: 19 381 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-apple-iphone-14-pro-max-858090?skuid=2345261")
    await message.answer_photo(photo="https://images.uzum.uz/cmus1nrifoubkc6qdj9g/original.jpg",
                               caption="Apple Iphone 14 pro"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 128gb"
                                       "\nPhone price💸: 17 613 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-apple-iphone-14-pro-857508?skuid=2345277")


@dp.message(F.text == "Samsung")
async def samsung(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/cmrienh25ku8ad8j4ie0/original.jpg",
                               caption="Samsung Galaxy A24"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 128gb"
                                       "\nPhone price💸: 2 499 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-samsung-galaxy-541795?skuid=1073303")
    await message.answer_photo(photo="https://images.uzum.uz/cmro6d9s99ouqbfsd5d0/original.jpg",
                               caption="Samsung Galaxy S22 Global"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 128gb"
                                       "\nPhone price💸: 7 499 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-samsung-galaxy-896696")
    await message.answer_photo(photo="https://images.uzum.uz/cmssut9s99ouqbfskkf0/original.jpg",
                               caption="Samsung Galaxy S22 Global"
                                       "\nCharger capacity🔋: 100💯"
                                       "\nPhone status📊: New box☑️"
                                       "\nPhone memory⚙️: 256gb"
                                       "\nPhone price💸: 15 000 000"
                                       "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-samsung-galaxy-896696?skuid=2375650")


@dp.message(F.text == "Oppo")
async def oppo(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/cjvj8usvutv76hn0cg8g/original.jpg", caption="OPPO A77s"
                                                                                                         "\nCharger capacity🔋: 100💯"
                                                                                                         "\nPhone status📊: New box☑️"
                                                                                                         "\nPhone memory⚙️: 128gb"
                                                                                                         "\nPhone price💸: 2 979 000"
                                                                                                         "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-oppo-a77s-8-gb128-gb-314784?skuid=1005481")
    await message.answer_photo(photo="https://images.uzum.uz/cjl0ln4vutv1g2rimd2g/original.jpg", caption="OPPO A17k"
                                                                                                         "\nCharger capacity🔋: 100💯"
                                                                                                         "\nPhone status📊: New box☑️"
                                                                                                         "\nPhone memory⚙️: 128gb"
                                                                                                         "\nPhone price💸: 1 590 000"
                                                                                                         "\nLearn more link➡️: https://uzum.uz/ru/product/smartfon-oppo-a17k-cph2471-364gb-navy-258090")


async def main():
    await dp.start_polling(bot)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Bot ishga qayta tushirish!"),
        BotCommand(command="/help", description="Yordam!")
    ])
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
