import smtplib
import datetime as dt
import random


MY_EMAIL = "lars@groundwave.se"
PW = ""
APPS = "apps@groundwave.se"
quotes_list = []




with open("quotes.txt") as quotes_file:
    lines = quotes_file.readlines()
    for line in lines:
        quotes_list.append(line.strip("\n"))


random_quote = random.choice(quotes_list)

t = dt.datetime.now()
day_number = t.weekday()

if day_number == 4:

    with smtplib.SMTP(host="mail.groundwave.se", port=587) as connection:
        connection.starttls()
        connection.login(user=APPS, password=PW)
        connection.sendmail(from_addr=APPS,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Quote of the week\n\n{random_quote}")

