import openai
from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle CORS if your frontend is on a different domain/port

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

openai_api_key = "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"  # Replace with your actual API key
openai.api_key = openai_api_key

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['user_input']

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # Or any other available model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        response_text = response['choices'][0]['message']['content']
    except Exception as e:
        response_text = f"An error occurred: {str(e)}"

    return jsonify({'message': response_text})

if __name__ == '__main__':
    app.run(debug=True)
