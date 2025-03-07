# 🌦️ Telegram Weather Bot

A **Telegram bot** that provides real-time weather updates using the **OpenWeather API**. Just type `/weather`, and the bot will ask for a city name, then return the current temperature, humidity, and weather conditions.

## 🚀 Features
✅ Interactive chat – asks for city name in real-time  
✅ Uses the latest `python-telegram-bot` v20+  
✅ Fetches **live weather data** from OpenWeather API  
✅ Simple `/start` and `/weather` commands  
✅ **Handles invalid city names gracefully**  

---

## 📦 Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/NadirAliOfficial/telegram-weather-bot.git
cd telegram-weather-bot
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Get Your OpenWeather API Key**
1. **Sign up** at [OpenWeather](https://home.openweathermap.org/users/sign_up).
2. Go to **API Keys Section** and generate a new key.
3. Copy your API key.

---

## 🎯 **Usage**

### 1️⃣ **Create a `.env` File**
Inside the project folder, create a `.env` file:
```
BOT_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_openweather_api_key
```

### 2️⃣ **Run the Bot**
```bash
python weather_bot.py
```

### 3️⃣ **Test on Telegram**
- Send **`/weather`**  
- The bot will ask for a city name.  
- Reply with a city (e.g., **London**), and the bot will return the weather.

---

## 🌍 **Deployment**
### 🔹 Deploy on Heroku
1. **Install the Heroku CLI**:
   ```bash
   npm install -g heroku
   ```
2. **Login to Heroku**:
   ```bash
   heroku login
   ```
3. **Create a Heroku app**:
   ```bash
   heroku create your-weather-bot
   ```
4. **Add a `Procfile`**:
   ```
   worker: python weather_bot.py
   ```
5. **Push to Heroku**:
   ```bash
   git add .
   git commit -m "Deploy Weather Bot"
   git push heroku main
   heroku ps:scale worker=1
   ```

### 🔹 Deploy on a VPS (Linux)
1. Upload the bot files to your server.
2. Run the bot in a **tmux** or **screen** session:
   ```bash
   python weather_bot.py &
   ```

---

## 📌 **Example Responses**
**Command:**
```
/weather
```
**Bot Response:**
```
📍 Please enter the city name to check the weather:
```

**User:**
```
London
```
**Bot Response:**
```
🌤 Weather in London:
🌡 Temperature: 18°C
💧 Humidity: 65%
📌 Condition: Clear Sky
```

---

## 🛠 **Troubleshooting**
❌ **"Invalid API Key" Error?**  
- Ensure your **API key is correct** in `.env`.  
- Wait **15-30 minutes** after creating a new key.  
- Test with:  
  ```python
  import os
  print(os.getenv("WEATHER_API_KEY"))
  ```

❌ **Bot Not Responding?**  
- Check if your Telegram bot token is correct.  
- Make sure `python-telegram-bot` is installed properly:  
  ```bash
  pip install --upgrade python-telegram-bot
  ```

---

## 📜 **Requirements.txt**
If you need to create `requirements.txt`, run:
```bash
pip freeze > requirements.txt
```
Or manually add:
```
python-telegram-bot
requests
python-dotenv
```

---

## 📌 **Contributing**
Feel free to **fork**, improve, or add new features to this bot. Pull requests are welcome! 🎉  

---

## 📝 **License**
This project is **open-source** and available under the **MIT License**.

---

### ⭐ If you found this useful, please consider giving the repository a **star** ⭐ on GitHub!
