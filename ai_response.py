import requests
import json

personality = ["extremely friendly", "friendly", "normal", "aggressive", "very aggressive"]

def ai_response(input):
    def get_ai_pick(input):
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
                                {"type": "text", "text": input},
                            ],
                        }
                    ],
                }
            ),
        )
        return response

    prompt = f"Tell a user with a {personality[4]} tone that they should go to {input['name']} (that you picked) for a meal. The restaurant is located at {input['vicinity']}. The restaurant has a rating of {input['rating']}."

    data_json = get_ai_pick(prompt).json()
    content = data_json["choices"][0]["message"]["content"]
    print(content)