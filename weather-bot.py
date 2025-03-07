import requests
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, ContextTypes

# Load environment variables from .env file
load_dotenv()

# Get tokens from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

# Dictionary to store user states (who requested weather)
user_states = {}

# Function to fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return "❌ Invalid city name. Please try again."

    weather_desc = response["weather"][0]["description"].title()
    temp = response["main"]["temp"]
    humidity = response["main"]["humidity"]

    return f"🌤 **Weather in {city.title()}**:\n🌡 Temperature: {temp}°C\n💧 Humidity: {humidity}%\n📌 Condition: {weather_desc}"

# Command to start the bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("🌍 Welcome to Weather Bot!\nSend **/weather** to get weather updates.")

# Command to initiate weather request
async def ask_for_city(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat_id
    user_states[user_id] = "awaiting_city"
    await update.message.reply_text("📍 Please enter the city name to check the weather:")

# Handle city input
async def city_response(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat_id

    if user_id in user_states and user_states[user_id] == "awaiting_city":
        city = update.message.text
        weather_info = get_weather(city)
        await update.message.reply_text(weather_info)

        # Clear user state after getting response
        del user_states[user_id]
    else:
        await update.message.reply_text("🤖 I didn't understand that. Send /weather to check the weather.")

# Main function to run the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", ask_for_city))
    
    # Handle city name input from users
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, city_response))

    # Start bot
    print("✅ Weather Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
