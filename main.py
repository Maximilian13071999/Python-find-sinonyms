import requests
from bs4 import BeautifulSoup

url = "https://sinonim.org/t/"

word = input("Введите слово").lower()

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
}

req = requests.get(url + word, headers=headers)
src = req.text
soup = BeautifulSoup(src, "lxml")
desc = soup.find("li").text
print(desc[0:desc.find("◆")])