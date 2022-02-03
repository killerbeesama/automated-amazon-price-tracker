import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

EMAIL = "<your email>"
PASSWORD = "<your password>"
RECEIVER_EMAIL = "<email>"

SET_PRICE = float("<PRICE AT WHICH YOU WANNA BUY>")

URl = "<paste amazon product links here>"

paramter = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
}
r = requests.get(url=URl, headers=paramter)
web_data = r.text

soup = BeautifulSoup(web_data, "lxml")
web_price_unclean = soup.select_one("span .a-offscreen")
price_cleaned = web_price_unclean.get_text().split('₹')[1].split(',')
price = float(price_cleaned[0] + price_cleaned[1])

message = "<your message>"

if price < SET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=f"subject:Happy Birthday\n\n{message}"
        )
