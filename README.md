# BlabToMePython

BlabToMe is a push notification service that supports pushing a 'Blab' to lots of different types of 'Endpoints'. 
These Endpoints include:
- Push to an iOS app
- Email
- SMS message
- Voice call with text to speech

This library will help you to send messages to endpoints. An example would be: 
```

#!/usr/bin/env python3
import requests
from BlabToMe import SendBlabToEndPoints

endpointToMessage = "EPOmJpyx1wCxOTBEygeH9vvnzdvZy167,EPUKqnxbYR24bV74Wxi9RUDtqR7gfNUw"
messageToBlab = "Message from Python Helper Library"
BlabUsername = "ThisIsMyUsername"
BlabPassword = "ThisIsNotASecurePassword"

makeRequest = SendBlabToEndPoints(BlabUsername, BlabPassword, messageToBlab, endpointToMessage)
print(makeRequest)


```
You can send the same message to lots of endpoints using a CSV of Endpoints, eg: 

endpointToMessage = "EP123abc,EP987zyx345,EP456mno"
