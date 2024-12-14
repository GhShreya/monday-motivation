import smtplib
import datetime as dt
import random
import credentials
# -------------------------DATA------------------------- #
with open(file="quotes.txt") as file:
    data = file.read()                   #Do this in one line data = file.readlines(), data is as list
    list = list(data.split("\n"))
    quote = random.choice(list)

# --------------------CURRENT DATE---------------------- #
date = dt.datetime.now()
day = date.strftime(format="%A")
my_email = credentials.SENDERMAIL
password = credentials.PASSWORD
if day == "Monday":
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs= credentials.RECEIVERMAIL,
                            msg=f"Subject:Motivation\n\n{quote}")
