import json
from typing import Any

import requests

from data_models import Location, RequestData


def generate_restaurant_search_query(user_message: str, starting_location: Location) -> RequestData:
    def prompt_ai(user_message: str) -> str:
        prompt = "\n\nWith this, write ONLY a JSON file without anything else which includes keyword (Cuisine or a specific food type or a word to represent all range of food like Chinese food) for the restaurant to eat, radius (in meters), min price and max price as parameters (keyword, radius, min_price, max_price) where price is from google maps 1-4 scale and only one JSON only"

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",
                "Content-Type": "application/json",
                "HTTP-Referer": "<YOUR_SITE_URL>",
                "X-Title": "<YOUR_SITE_NAME>",
            },
            data=json.dumps(
                {
                    "model": "google/gemini-2.0-pro-exp-02-05:free",
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": user_message + prompt},
                            ],
                        }
                    ],
                }
            ),
        )

        raw_response: dict[str, Any] = response.json()
        content: str = raw_response["choices"][0]["message"]["content"]
        return content.replace("```json", "").replace("```", "").strip()

    request_data = RequestData(
        location=starting_location,
        radius=1000,  # 5 km radius
    )
    while True:
        try:
            raw_request: dict[str, Any] = json.loads(prompt_ai(user_message))
            request_data.radius = raw_request.get("radius") or request_data.radius
            request_data.keyword = raw_request.get("keyword")
            request_data.min_price = raw_request.get("min_price")
            request_data.max_price = raw_request.get("max_price")
            break
        except json.JSONDecodeError as e:
            print(e)

    return request_data
