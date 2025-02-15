import os
from dotenv import load_dotenv
import requests

from dataModels import Location, RequestData

# Load environment variables from .env file
load_dotenv(dotenv_path="credentials/credentials.env")

# Access the API key
api_key = os.getenv("API_KEY")
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
detailUrl = "https://maps.googleapis.com/maps/api/place/details/output?"


def findResturants(requestData: RequestData) -> dict:
    response = requests.get(generateRequest(requestData))
    print(generateRequest(requestData))
    return response.json()


def generateRequest(requestData: RequestData) -> str:
    request = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    data = requestData.toDict()

    request += f"location={data['location'].latitude}%2C{data['location'].longitude}"

    for key in data:

        if data[key] is not None and key != "location":
            request += f"&{key}={data[key]}"

    request += f"&type=restaurant"
    request += f"&key={api_key}"
    return request


def getDetails(place_id: str) -> dict:
    request = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,rating,reviews,business_status,opening_hours,user_ratings_total,serves_vegetarian_food,serves_wine,serves_beer,formatted_address&key={api_key}"
    response = requests.get(request)
    return response.json()


if __name__ == "__main__":
    print("hello world")
    sfu_burnaby_location = Location(longitude=-122.9199, latitude=49.2781)

    # Create a dummy Request object
    dummy_request = RequestData(
        location=sfu_burnaby_location,
        radius=1000,  # 1 km radius
        keyword="pizza",
        language="en",
        min_price=1,
        max_price=4,
        open_now=True,
        rank_by="prominence",
    )

    # Get the response from the findRestaurants function
    responses = findResturants(dummy_request)["results"]

    # Print the top response formatted for human view and get details
    if responses:
        top_response = responses[0]
        print("Top Response:")
        print(f"Name: {top_response['name']}")
        print(f"Address: {top_response['vicinity']}")
        print(f"Rating: {top_response.get('rating', 'N/A')}")
        print(f"User Ratings Total: {top_response.get('user_ratings_total', 'N/A')}")

        # Get place details
        place_id = top_response["place_id"]
        details = getDetails(place_id)
        print("\nPlace Details:")
        print(f"Name: {details['result'].get('name', 'N/A')}")
        print(f"Rating: {details['result'].get('rating', 'N/A')}")
        print(f"Reviews: {details['result'].get('reviews', 'N/A')}")
        print(f"Business Status: {details['result'].get('business_status', 'N/A')}")
        print(f"Opening Hours: {details['result'].get('opening_hours', 'N/A')}")
        print(f"User Ratings Total: {details['result'].get('user_ratings_total', 'N/A')}")
        print(f"Serves Vegetarian Food: {details['result'].get('serves_vegetarian_food', 'N/A')}")
        print(f"Serves Wine: {details['result'].get('serves_wine', 'N/A')}")
        print(f"Serves Beer: {details['result'].get('serves_beer', 'N/A')}")
        print(f"Address: {details['result'].get('formatted_address', 'N/A')}")

        print("\nReviews:")
        reviews = details["result"].get("reviews", [])
        if reviews:
            for review in reviews:
                print(f"Author: {review.get('author_name', 'N/A')}")
                print(f"Rating: {review.get('rating', 'N/A')}")
                print(f"Text: {review.get('text', 'N/A')}")
                print(f"Time: {review.get('relative_time_description', 'N/A')}")
                print("-" * 40)
        else:
            print("No reviews found.")
    else:
        print("No responses found.")
