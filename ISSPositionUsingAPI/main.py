import requests
import datetime as dt
import smtplib

MY_EMAIL = "Your Email"
MY_PASSWORD = "Your Email Password"
MY_LAT = 18.6783
MY_LNG = 73.8950


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LAT-5 <= latitude >= MY_LAT+5 and MY_LNG-5 <= longitude >= MY_LNG+5:
        return True


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_hr = dt.datetime.now().hour
    return sunset <= time_hr <= sunrise


if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look UP👆\n\nThe International Space Station is in the sky"
        )


