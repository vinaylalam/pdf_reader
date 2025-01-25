import PyPDF2
import requests
import json

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

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

# Example usage
api_key = "AIzaSyAmCxy6GIdM84Gq1ZHg-V1lvpCnY3vGIGg"
pdf_file_path = 'path/to/your/document.pdf'
document_text = read_pdf('/Users/vinay/Documents/docproject/test.pdf')

while True:
    user_question = input("Enter your question (or 'exit' to quit): ")
    if user_question.lower() == 'exit':
        break
    answer = answer_question(user_question, api_key)
    print(f"Answer: {answer}")
