import requests
import json

input = "I want to eat something salty, what should I eat in 10 words?"

response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "google/gemini-2.0-pro-exp-02-05:free",
        "messages": [
    {
        "role": "user",
        "content": [
        {
            "type": "text",
            "text": input
        },
        ]
    }
    ],
})
)

data = response.json()
content = data['choices'][0]['message']['content']
print(content)

