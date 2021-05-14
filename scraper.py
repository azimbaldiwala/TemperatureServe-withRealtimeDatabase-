import requests
from bs4 import BeautifulSoup


def get_values():
    try:

        url = "http://192.168.1.110"
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        temperature = soup.find(id='temperature').text
        humidity = soup.find(id='humidity').text
        return temperature, humidity

    except:

        return "Error", "Error"
