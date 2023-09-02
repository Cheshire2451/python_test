import requests
from bs4 import BeautifulSoup
for count in range(1,8):
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="w-full rounded border")


    for i in data:
        price = i.find('h5').text
        name = i.find('h4').text
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
        print(name +"\n" + price + "\n" + url_img)

