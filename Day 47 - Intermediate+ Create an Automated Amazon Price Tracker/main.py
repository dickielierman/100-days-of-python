from bs4 import BeautifulSoup
import requests as req
import smtplib
from env import *
headers = {
    "Accept-Language":'en-US,en;q=0.9',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

products_to_watch = {
    "ANYCUBIC Grey Resin": {
        "price": "39.99",
        "url": "https://www.amazon.com/ANYCUBIC-UV-Curing-Precision-Excellent-Fluidity/dp/B07G3663HD/ref=sr_1_4?crid=18OPTBMWPH172&keywords=ANYCUBIC+3D+Printer+Resin&qid=1655166023&s=industrial&sprefix=anycubic+3d+printer+resin%2Cindustrial%2C61&sr=1-4"}}

for name, data in products_to_watch.items():
    res = req.get(data["url"], headers=headers)
    amazon_resin = res.text
    soup = BeautifulSoup(amazon_resin, "html.parser")
    product_name = soup.find(id="productTitle").get_text().strip()
    price_block = soup.find(id="apex_desktop_newAccordionRow")
    product_price = float(price_block.select_one(selector='.a-price .a-offscreen').get_text().strip().replace("$", ""))
    if product_price < float(data["price"]):
        message = f"{product_name} is selling for {product_price}"
        with smtplib.SMTP(YAHOO_SMTP, port=587, timeout=120) as connection:
            connection.starttls()
            connection.login(user=YAHOO_EMAIL, password=YAHOO_PASSWORD)
            connection.sendmail(from_addr=YAHOO_EMAIL, to_addrs='richard.lierman@liermanintl.com', msg=f"Subject:LOW PRICE!!!: {name}\n\n{message}")