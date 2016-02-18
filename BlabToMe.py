#!/usr/bin/env python3

import requests

def SendBlabToEndPoints(BlabToMeUsername, BlabToMePassword, BlabMessage, EndPointCSV)
POSTPayLoad = {'userName': BlabToMeUsername, 'Password': BlabToMePassword, 'Message':'BlabMessage', 'SendTo':'EndPointCSV'}
r = requests.post("http://httpbin.org/post", auth=(username, BlabToMePassword), data=POSTPayLoad)
r.json()
