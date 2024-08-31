"""
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": False
}' 

"""

import requests
import json

url = 'http://localhost:11434/api/generate'
data = {
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": False
  }

headers = {
  "Content-Type": "application/json"
}
response = requests.post(url, json = data,headers = headers)

response = json.loads(response.text)


print(response["response"])

