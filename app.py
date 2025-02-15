import os

from dotenv import load_dotenv
from flask import Flask, render_template, request

import ai_api
from data_models import Location
import google_maps_manager

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv(dotenv_path="credentials/credentials.env")
api_key = os.getenv("API_KEY")
nearby_search_base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
details_base_url = "https://maps.googleapis.com/maps/api/place/details/json"
sfu_burnaby_location = Location(longitude=-122.9199, latitude=49.2781)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    results = None  # Default is no results

    if request.method == "POST":
        query = request.form.get("query")

        # query is the response, use to get the value from the user input
        if query:
            request_data = ai_api.generate_restaurant_search_query(query, sfu_burnaby_location)
            resuts = google_maps_manager.find_restaurants(request_data, nearby_search_base_url, api_key)["results"]
            results = [{"name": f"Best {query} Restaurant"}]

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
