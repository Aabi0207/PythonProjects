import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = "CMV0OPBCFZ5EJ7M3"
news_api_key = "340e7a18429147e482d8ffdb0444ff52"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_api_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key
}

stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_api_parameters)
stock_response.raise_for_status()
print(stock_response.status_code)

tesla_share_data = stock_response.json()
print(tesla_share_data)

required_dates = [date for date in tesla_share_data["Time Series (Daily)"]]

yesterday_closing_price = float(tesla_share_data["Time Series (Daily)"][required_dates[0]]["4. close"])
day_before_yesterday_closing_price = float(tesla_share_data["Time Series (Daily)"][required_dates[1]]["4. close"])

percentage_increase = (yesterday_closing_price - day_before_yesterday_closing_price)/day_before_yesterday_closing_price * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_api_parameters = {
    "q": "tesla",
    "from": required_dates[1],
    "sortBy": "popularity",
    "apikey": news_api_key
}
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_parameters)
news_response.raise_for_status()
news_data = news_response.json()
print(news_data)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
rounded_percentage = round(percentage_increase)
if rounded_percentage > 0:
    tesla_stock_status = f"TSLA: 🔺{abs(rounded_percentage)}%"
if rounded_percentage < 0:
    tesla_stock_status = f"TSLA: 🔻{abs(rounded_percentage)}%"

twilio_account_sid = "AC751d627c43755c645d4d8fddbc4ae34c"
twilio_auth_token = "8f881b57693f5c51b27c574cf8890d4f"
client = Client(twilio_account_sid, twilio_auth_token)
for i in range(3):
    message = client.messages.create(
      body=f"{tesla_stock_status}\nHeadline: {news_data['articles'][i]['title']}\n"
           f"brief: {news_data['articles'][i]['description']}",
      from_="+13613043716",
      to="+917276622705"
    )
    print(message.status)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

