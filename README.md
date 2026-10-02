# Telegram Weather Bot

A Telegram bot that fetches real-time weather updates using the OpenWeatherMap API.

**Description**
This bot integrates with Telegram to provide users with current weather information for any city. It retrieves data from the OpenWeatherMap service and presents temperature, humidity, and weather conditions directly in the chat.

## Features
- Current weather by city name
- Temperature, humidity, wind speed
- Simple command interface

## Requirements
```
pip install python-telegram-bot requests
```

*Alternatively, install all dependencies via the provided requirements file:* 
```
pip install -r requirements.txt
```

## Setup
```python
BOT_TOKEN = "your_telegram_token"
WEATHER_API_KEY = "your_openweathermap_key"
```

## Configuration
Create a `.env` file in the project root with the following variables:
```
BOT_TOKEN=your_telegram_token
WEATHER_API_KEY=your_openweathermap_key
```
These variables are loaded at runtime using `python-dotenv`.

```bash
python weather-bot.py
```

## Commands
- `/weather <city>` — get current weather
- `/help` — show available commands

## Usage
Run the bot with:
```
python weather-bot.py
```
The bot will start polling Telegram for messages.

## Project Structure
```
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── weather-bot.py
└── .env (not tracked, created by user)
```

## License
MIT
<!-- updated: 2025-10-26-r01 -->
