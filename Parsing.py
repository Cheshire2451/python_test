# https://scrapingclub.com/exercise/list_basic/?page=1
import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

def get_url():

    for count in range(1, 8):
        sleep(1)
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="w-full rounded border")

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url


for card_url in get_url():
    response = requests.get(card_url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find("div", class_="my-8 w-full rounded border")

    name = data.find("h3", class_="card-title").text
    price = data.find("h4", class_="my-4 card-price").text
    textar = data.find("p", class_="card-description").text
    url_img = "https://scrapingclub.com" + data.find("img").get("src")
    print(name + "\n" + price + "\n" + url_img + "\n" + textar)

    # name + "\n" + price + "\n" + url_img + "\n" + textar




    #     price = i.find('h5').text
    #     name = i.find('h4').text
    #     url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
    #     print(name + "\n" + price + "\n" + url_img)
