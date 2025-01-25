import requests
import json

def answer_question(question, api_key):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [{
            "parts": [{"text": question}]
        }]
    }
    
    response = requests.post(url, headers=headers, params={"key": api_key}, json=payload)
    
    if response.status_code == 200:
        return response.json()  # Adjust based on the actual response structure
    else:
        return f"Error: {response.status_code}, {response.text}"
