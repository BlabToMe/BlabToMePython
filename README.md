# BlabToMePython

BlabToMe is a push notification service that supports pushing a 'Blab' to lots of different types of 'Endpoints'. 
These Endpoints include:
- Push to an iOS app
- Email
- SMS message
- Voice call with text to speech

This library will help you to send messages to endpoints. An example would be: 
"
#!/usr/bin/env python3
import requests
import BlabToMe
endpointToMessage = "EP123abc"
messageToBlab = "Hey this is my message"
BlabUsername = "ThisIsMyUsername"
BlabPassword = "ThisIsMyUnsecuredPassword"

SendBlabToEndPoints(BlabUsername, BlabPassword, BlabMessage, endpointToMessage)
"
You can send the same message to lots of endpoints using a CSV of Endpoints, eg: 

endpointToMessage = "EP123abc,EP987zyx345,EP456mno"
