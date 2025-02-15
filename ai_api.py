import requests
import json

user_input = "I want some soup that's in 10km within me"
prompt = ". With this, write ONLY a JSON file without anything else which includes keyword (Cuisine or a specific food type or a word to represent all range of food like Chinese food) for the restaurant to eat, radius (in meters), min price and max price as parameters (keyword, radius, min_price, max_price) where price is from google maps 1-4 scale and only one JSON only"

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>",
        "X-Title": "<YOUR_SITE_NAME>",
    },
    data=json.dumps({
        "model": "google/gemini-2.0-pro-exp-02-05:free",
        "messages": [
    {
        "role": "user",
        "content": [
        {
            "type": "text",
            "text": user_input + prompt
        },
        ]
    }
    ],
})
)

data_json = response.json()
content = data_json['choices'][0]['message']['content']
cleaned_content = content.replace("```json", "").replace("```", "").strip()
print(cleaned_content)
data = json.loads(cleaned_content)
print(data)