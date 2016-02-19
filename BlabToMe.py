#!/usr/bin/env python3
import requests

def SendBlabToEndPoints(BlabToMeUsername, BlabToMePassword, BlabMessage, EndPointCSV):
  POSTPayLoad = {'UserName': BlabToMeUsername, 'Password': BlabToMePassword, 'Message':BlabMessage, 'SendTo':EndPointCSV}
  r = requests.post("https://api.blabto.me/Inbound/Inbound", auth=(BlabToMeUsername, BlabToMePassword), data=POSTPayLoad)
  if r.status_code == 401:
    return '{"Success":false,"Response":"Username and Password are not correct"}'
  else:
    return r.json()

def GetBlabsForUser(BlabToMeUsername, BlabToMePassword):
  POSTPayLoad = {'UserName': BlabToMeUsername, 'Password': BlabToMePassword}
  r = requests.post("https://api.blabto.me/API/GetBlabsForUser", auth=(BlabToMeUsername, BlabToMePassword), data=POSTPayLoad)
  if r.status_code == 401:
    return '{"Success":false,"Response":"Username and Password are not correct"}'
  else:
    return r.json()
  
def GetBlabsForEndPoint(BlabToMeUsername, BlabToMePassword, EndPointToQuery):
  POSTPayLoad = {'UserName': BlabToMeUsername, 'Password': BlabToMePassword, 'Endpoint':EndPointToQuery}
  r = requests.post("https://api.blabto.me/API/GetBlabsForUser", auth=(BlabToMeUsername, BlabToMePassword), data=POSTPayLoad)
  if r.status_code == 401:
    return '{"Success":false,"Response":"Username and Password are not correct"}'
  else:
    return r.json()
  
