import datetime as dt
import random
import smtplib
import pandas as pd


def randomletter(name):
    k = random.randint(1, 3)
    file_path = f"letter_templates/letter_{k}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", name)
    return contents


def sendemail(email_address, name):
    username = "YOUR-EMAIL"
    password = "YOUR-PASSWORD"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=username, password=password)
    connection.sendmail(from_addr=username,
                        to_addrs=email_address,
                        msg=f"Happy Birthday! \n\n {randomletter(name)}")
    connection.close()



now = dt.datetime.now()
today_date = int(now.strftime("%d"))
today_month = int(now.strftime("%m"))

birthday_data = pd.read_csv("birthdays.csv")
n = len(birthday_data.index)
for i in (0, n - 1):
    if today_date == birthday_data.day[i]:
        if today_month == birthday_data.month[i]:
            uname = birthday_data.name[i]
            uaddress = birthday_data.email[i]
            sendemail(uaddress, uname)
