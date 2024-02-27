# Python
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    answer = None
    url = None
    if request.method == 'POST':
        url = request.form.get('url')
        question = request.form.get('question')

        headers = {"Authorization": "Bearer EDEN_API_KEY"}
        api_url = "https://api.edenai.run/v2/image/question_answer"
        data = {
            "providers": "openai",
            "file_url": url,
            "question": question,
            "fallback_providers": ""
        }

        response = requests.post(api_url, json=data, headers=headers)
        result = json.loads(response.text)
        if 'openai' in result and 'answers' in result['openai']:
            answer = result['openai']['answers']
        else:
            answer = "No answer found."

    return render_template('index.html', answer=answer, url=url)

if __name__ == '__main__':
    app.run(debug=True)
