# CryptoBot

CryptoBot is a Python-based Telegram bot that monitors cryptocurrency prices in real-time using the Binance WebSocket API. The bot sends notifications to a specified user when the price of a cryptocurrency undergoes a significant change.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/FlacSy/CryptoBot.git
cd CryptoBot
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Telegram Bot token and user ID:

```env
BOT_TOKEN=your_telegram_bot_token
USER_ID=your_telegram_user_id
```

4. Create a `config.yaml` file with a list of cryptocurrency symbols to monitor:

```yaml
SYMBOLS:
  - btcusdt
  - ethusdt
  # Add more symbols as needed
```

## Usage

Run the main script to start the bot:

```bash
python main.py
```

The bot will connect to the Binance WebSocket API for each specified symbol and notify you when the price changes significantly.

## Customization

- Adjust the notification threshold in the `binance_ws` function (`price_diff > 5.0`) to control when notifications are sent.

## Contributors

- [FlacSy](https://github.com/FlacSy)

