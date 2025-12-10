"""
Quick connectivity test for Google's Gemini API.

Run:
    GEMINI_API_KEY=your-key python test.py
"""

import os
import sys

import requests

# GEMINI_API_KEY = "os.getenv... example"


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash")
print(f"Using model: {MODEL}")
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


def call_gemini(prompt: str) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY (or apikey) is not set in the environment.")

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                ]
            }
        ]
    }
    response = requests.post(
        ENDPOINT,
        params={"key": GEMINI_API_KEY},
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    data = response.json()
    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        return f"Unexpected response: {data}"


if __name__ == "__main__":
    test_prompt = "Provide two bullet points explaining why Gemini connectivity test succeeded."
    try:
        completion = call_gemini(test_prompt)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Gemini test failed: {exc}", file=sys.stderr)
        sys.exit(1)

    print("Gemini API test response:\n")
    print(completion)
