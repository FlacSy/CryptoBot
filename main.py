import asyncio
import json
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
import websockets
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
USER_ID = int(os.getenv('USER_ID'))
CONFIG_FILE = "config.yaml"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Dictionary to store previous prices for each symbol
previous_prices = {}

async def send_notification(symbol, price):
    await bot.send_message(USER_ID, f"Цена {symbol.upper()}: {price} USDT", parse_mode=ParseMode.MARKDOWN)

async def binance_ws(symbol):
    url = f"wss://stream.binance.com:9443/ws/{symbol.lower()}@trade"
    async with websockets.connect(url) as ws:
        while True:
            response = await ws.recv()
            data = json.loads(response)
            price = float(data['p'])

            # Check if the symbol is already in the dictionary
            if symbol in previous_prices:
                # Check if the difference is significant (you can adjust the threshold)
                price_diff = abs(price - previous_prices[symbol])
                if price_diff > 5:  # You can adjust the threshold as needed
                    await send_notification(symbol, price)

            # Update the previous price for the symbol
            previous_prices[symbol] = price

async def start_ws_tasks(symbols):
    tasks = [binance_ws(symbol) for symbol in symbols]
    await asyncio.gather(*tasks)

async def on_startup(dp):
    await bot.send_message(USER_ID, "Бот запущен и следит за изменениями курса валют!")

if __name__ == '__main__':
    from aiogram import executor

    with open(CONFIG_FILE, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    symbols = config_data.get('SYMBOLS', [])

    loop = asyncio.get_event_loop()
    loop.create_task(start_ws_tasks(symbols))
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
