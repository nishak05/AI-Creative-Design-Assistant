import os
import requests
import json

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_design_copy(title, tone="energetic"):

    if not OPENAI_API_KEY:
        print("ERROR: API key not loaded")
        return {"subtitle": "AI key missing", "cta": ""}

    prompt = f"""
You are a creative marketing assistant.

Generate:
1. A short subtitle (max 8 words)
2. A call-to-action (max 5 words)

Event title: "{title}"
Tone: {tone}

Return strictly in JSON format like:

{{
  "subtitle": "...",
  "cta": "..."
}}
"""

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.8
        }
    )

    if response.status_code != 200:
        print("API ERROR:", response.text)
        return {"subtitle": "AI error occurred", "cta": ""}

    data = response.json()
    content = data["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        print("JSON PARSE ERROR:", content)
        return {"subtitle": content.strip(), "cta": ""}