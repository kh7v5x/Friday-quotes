# 📩 Friday Islamic Reminder Email Bot

A simple Python automation script that sends a random Islamic reminder (quote) to your email every Friday using Gmail SMTP.

This project demonstrates:

Working with datetime

Reading from files

Random selection

Sending emails using smtplib

Basic automation logic

# 🚀 How It Works

The script checks today's weekday using datetime.

If today is Friday (weekday() == 4 → adjust if needed), it:

Opens a file named fridayqoutes

Selects a random quote

Sends it to your email via Gmail SMTP

# 🛠 Requirements

Python 3.x

Internet connection

Gmail account

# Built-in Python libraries used:

smtplib

datetime

random

No external installations required.

# 🔐 Gmail Setup (IMPORTANT)

Google blocks normal password login by default.

Option 1 (Recommended): Use App Password

Enable 2-Step Verification on your Google account.

Go to Google Account → Security → App Passwords.

Generate a new app password.

Replace this in your code:

MY_PASSWORD = "your_generated_app_password"
