❤️ Tinder Auto-Swiper Bot
An automated bot built using Selenium to log into Tinder via Facebook and automatically swipe left (dislike) on profiles. Great for learning browser automation and dealing with dynamic web elements.

✨ Features
🔐 Logs into Tinder using Facebook credentials

🧭 Handles popups like cookie consents and location permissions

💔 Automatically swipes left on profiles (dislike)

📱 Detects and dismisses Tinder match popups

🔄 Switches browser windows for Facebook login

📦 Requirements
Python 3.x+

Google Chrome installed

ChromeDriver (must match your Chrome version)

Environment variables for login

email=your_facebook_email
password=your_facebook_password
Required Libraries:

pip install selenium python-dotenv
🚀 How to Run
Clone or download this repository.

Install dependencies:

pip install selenium python-dotenv
Download and place the correct ChromeDriver in your system path:

Download ChromeDriver

Create a .env file with your Facebook credentials:

email=your_email@example.com
password=your_facebook_password
Run the bot:

python main.py
🎮 How It Works
✅ Uses Selenium to open Tinder, click "Log in with Facebook".

🔁 Switches to the Facebook login window, fills in credentials, and logs in.

💬 Handles cookie prompts, notification popups, and location permission requests.

🖱 Automatically clicks the dislike button 10 times.

⚠ Detects popups like “It’s a Match” and closes them if they interrupt the flow.

🧩 Future Enhancements
❤️ Add ability to swipe right (like) with criteria

🕵️‍♂️ Implement profile filters (bio/age/picture check)

📊 Collect data on swipe success rate

🤖 Use undetectable browser automation tools like Selenium Stealth

⚠️ Disclaimer
This bot is for educational purposes only. Automating interactions on dating platforms may violate Tinder's Terms of Service and could result in account suspension or banning. Use responsibly.

