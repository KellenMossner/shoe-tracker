from bs4 import BeautifulSoup
import requests
import smtplib
import ssl
from email.message import EmailMessage

# List of shoes to scrape prices for
shoes = {'vomero': 3299.90, 'pegasus%20plus': 3399.90, 'novablast': 2999.90}
shoes_on_sale = {'vomero': {'price':2300, 'link': 'https://www.sportsmanswarehouse.co'}}

def scrape_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to scrape {url}")
    return soup

def scrape_shoes(url, shoe):
    soup = scrape_url(url)
    listings = soup.select('.card-body')
    
    for listing in listings:
        price_element = listing.select_one('.price')
        if price_element:
            price_text = price_element.text.strip()
            price = price_text.replace('R', '').replace('\xa0', '').replace(',', '').strip()
            price = float(price)
            
            if price < shoes[shoe]:
                link = listing.select_one('.title a')['href']
                shoes_on_sale[shoe] = {'price': price, 'link': link}

def notify():
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "emailbotkellen@gmail.com"
    sender_password = "gjsc xjpi dboh szbh"
    receiver_email = "Kellenmossner@gmail.com"

    subject = "Shoes on Sale"
    body = "The following shoes are on sale:\n\n"
    for shoe, details in shoes_on_sale.items():
        body += f"{shoe}: R{details['price']} - {details['link']}\n"

    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = receiver_email
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, em.as_string())
        print("Email sent successfully!")
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")

# Rest of the code remains the same

def main():
    # base_url = 'https://www.sportsmanswarehouse.co.za/products/?keyword='
    
    # for shoe in shoes.keys():
    #     url = base_url + shoe + '&filters%5Bcategories%5D%5B%5D=5771'
    #     print(url)
    #     scrape_shoes(url, shoe)
        
    if shoes_on_sale:
        notify()     

if __name__ == "__main__":
    main()