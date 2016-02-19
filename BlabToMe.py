#!/usr/bin/env python3

import requests

def SendBlabToEndPoints(BlabToMeUsername, BlabToMePassword, BlabMessage, EndPointCSV)
  POSTPayLoad = {'userName': BlabToMeUsername, 'Password': BlabToMePassword, 'Message':'BlabMessage', 'SendTo':'EndPointCSV'}
  r = requests.post("https://api.blabto.me/Inbound/Inbound", auth=(username, BlabToMePassword), data=POSTPayLoad)
  if r.status_code = 404:
    return "{"Success":false,"Response":"Username and Password are not correct"}"
  else:
    return r.json()

def GetBlabsForUser(BlabToMeUsername, BlabToMePassword)
  POSTPayLoad = {'userName': BlabToMeUsername, 'Password': BlabToMePassword}
  r = requests.post("https://api.blabto.me/API/GetBlabsForUser", auth=(username, BlabToMePassword), data=POSTPayLoad)
  if r.status_code = 404:
    return "{"Success":false,"Response":"Username and Password are not correct"}"
  else:
    return r.json()
  
def GetBlabsForEndPoint(BlabToMeUsername, BlabToMePassword, EndPointToQuery)
  POSTPayLoad = {'userName': BlabToMeUsername, 'Password': BlabToMePassword, 'Endpoint':EndPointToQuery}
  r = requests.post("https://api.blabto.me/API/GetBlabsForUser", auth=(username, BlabToMePassword), data=POSTPayLoad)
  if r.status_code = 404:
    return "{"Success":false,"Response":"Username and Password are not correct"}"
  else:
    return r.json()
  
