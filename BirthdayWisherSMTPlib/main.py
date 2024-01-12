from datetime import datetime
import pandas
import smtplib

MY_EMAIL = "Your Email"
MY_PASSWORD = "Your Password"

today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("Birthday_wisher/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
