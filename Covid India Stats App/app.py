import credentials
from flask import Flask, request
import requests
app = Flask(__name__)


# Adds support for GET requests to our webhook
@app.route('/webhook', methods=['GET'])
def webhook():
    verify_token = request.args.get("hub.verify_token")
    # Check if sent token is correct
    if verify_token == "abc":
        # Responds with the challenge token from the request
        return request.args.get("hub.challenge")
    return 'Unable to authorise.'


@app.route("/webhook", methods=['POST'])
def webhook_handle():
    output = request.get_json()
    print(output)
    message = output['entry'][0]['messaging'][0]['message']
    sender_id = output['entry'][0]['messaging'][0]['sender']['id']
    if message['text'] == "Hello":
        request_body = {
            'recipient': {
                'id': sender_id
            },
            'message': {"text": "hello, world!"}
        }
        response = requests.post('https://graph.facebook.com/v5.0/me/messages?access_token=EAALWPZAiZB5dwBABbi98woPPOROy7F0HnmO4kdIehvTy4q2XeQnmhxZATCAr1M0cMV54lUkZAFzaeAYbBKklfS9aOgruZAau0Nv04SpU8EQxOhkLcZCVdxDqLxQBZAnRlZCM6TDGSfZAwcAFqykfHzFosHo0l5Ol5osHFMR4QkLnh0LMZArBarydXb0qJoZBdGgqcYZD',
                                json=request_body).json()
    return 'ok'


if __name__ == "__main__":
    app.run()
