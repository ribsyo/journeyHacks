import os
from dotenv import load_dotenv
import requests

from dataModels import Location, RequestData
# Load environment variables from .env file
load_dotenv(dotenv_path='credentials/credentials.env')

# Access the API key
api_key = os.getenv('API_KEY')
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'


def findResturants(requestData: RequestData) -> dict:
    response = requests.get(generateRequest(requestData))
    print(generateRequest(requestData))
    return response.json()

def generateRequest(requestData: RequestData) -> str:
    request = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
    data = requestData.toDict()

    request += f"location={data['location'].latitude}%2C{data['location'].longitude}"

    for key in data:

        if data[key] is not None and key != "location":
            request += f"&{key}={data[key]}"

    request += f"&type=restaurant"
    request += f"&key={api_key}"
    return request

if __name__ == "__main__":
    print("hello world")