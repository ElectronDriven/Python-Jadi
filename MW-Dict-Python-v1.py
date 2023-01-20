import requests as req
import json

apiURL = ('https://www.dictionaryapi.com/api/v3/references/learners/json/apple?key=b0cb0b67-8976-404a-b250-9b27d60464c3')
apiKey = ('b0cb0b67-8976-404a-b250-9b27d60464c3')

apiURL2 = ('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&past_days=10&hourly=temperature_2m,relativehumidity_2m,windspeed_10m')

definition = []
#response = req.get(apiURL)
response = req.get(apiURL2)

#json_response = (json.loads(response))

#print(json_response)

print(response.json())