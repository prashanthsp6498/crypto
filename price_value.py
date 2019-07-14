#! /usr/bin/python3.7
import requests
import playsound
from bs4 import BeautifulSoup


old_value = 0
try:
    while True:
        try:
            resp = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
        except Exception as e:
            print("Check your connection\n")
            exit()
            
        soup = BeautifulSoup(resp.text, 'html.parser')
        value = float(soup.find(class_="details-panel-item--price__value").get_text())
        print("Bitcoin is very volatile", end="\r")
        if value > old_value:
            old_value = value
            playsound.playsound("you_suffer.mp3")
        elif value < old_value:
            old_value = value
            playsound.playsound("you_suffer.mp3")
except Exception as e:
    print("Thanks ahhh")
