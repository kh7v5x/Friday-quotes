import smtplib
import datetime as dt
import random

MY_EMAIL = "example@gmail.com" #add your email here
MY_PASSWORD = 'qWeRtY1234' #refer to readme

today = dt.datetime.now()
day = today.weekday()
if day == 2:
    with open('fridayqoutes') as islamic_reminders:
        all_lines = islamic_reminders.readlines()
        quote = random.choice(all_lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL, #enter recipient address here.
            msg=f'Subject: friday quotes\n\n{quote}'
        )

