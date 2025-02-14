import os
from dotenv import load_dotenv
import requests
# Load environment variables from .env file
load_dotenv(dotenv_path='credentials/credentials.env')

# Access the API key
api_key = os.getenv('API_KEY')
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters'

# https://places.googleapis.com/v1/places/GyuEmsRBfy61i59si0?fields=addressComponents&key=YOUR_API_KEY


# nearby seach url
# https://maps.googleapis.com/maps/api/place/nearbysearch/output?parameters

'''
https://maps.googleapis.com/maps/api/place/nearbysearch/json
  ?keyword=cruise
  &location=-33.8670522%2C151.1957362
  &radius=1500
  &type=restaurant
  &key=YOUR_API_KEY
'''

def testRequest() -> dict:
    
    response = requests.get(url)
    return response.json()



if __name__ == "__main__":
    print(testRequest())