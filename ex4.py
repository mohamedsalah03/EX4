# -*- coding: utf-8 -*-
from lxml import html
import requests


while True:
    turl = input("Enter Twitter URL: ")
    url = turl
    
    # request Twitter web page
    page = requests.get(url)
    tree = html.fromstring(page.content)

    # search for the Profile Nav Bar using Xpath
    navBar = tree.xpath('//span[@class="ProfileNav-value"]/text()')
    
    # the follower number is 3rd item
    number_follower=navBar[2]
    
    # print the follower
    print("Follower:" ,str(number_follower))

#15 minutes