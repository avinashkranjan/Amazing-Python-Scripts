import json
from flask import Flask, request
import requests
# Token that has to be generated from webhook page portal
ACCESS_TOKEN = "random token"
# Token that has to be added for verification with developer portal
VERIFICATION_TOKEN = "abc"
# Identifier payloads for initial button
C19INDIA = "C19INDIA"
app = Flask(__name__)


# This get endpoint is for verification with messenger app
@app.route('/webhook', methods=['GET'])
def webhook():
    verify_token = request.args.get("hub.verify_token")
    if verify_token == VERIFICATION_TOKEN:
        return request.args.get("hub.challenge")
    return 'Unable to authorise.'


@app.route("/webhook", methods=['POST'])
def webhook_handle():
    data = request.get_json()

    if data["object"] == "page":  # To verify that the request is being originated from a page

        for entry in data["entry"]:
            for event in entry["messaging"]:

                if event.get("message"):  # somebody typed a message
                    process_message(event)
                # user clicked/tapped "postback" button in earlier message
                elif event.get("postback"):
                    process_postback(event)
    return 'ok'


def process_message(event):
    # the facebook ID of the person sending you the message
    sender_id = event["sender"]["id"]

    # could receive text or attachment but not both
    if "text" in event["message"]:
        send_initial_menu(sender_id)


def send_initial_menu(sender_id):
    message_data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "Covid India Stats",
                        "subtitle": "Get the covid19 stats of Indian states",
                        "buttons": [{
                            "type": "web_url",
                            "url": "https://www.worldometers.info/coronavirus/country/india/",
                            "title": "Open Worldometer India"
                        }, {
                            "type": "postback",
                            "title": "Get Stats By Indian States",
                            "payload": C19INDIA,
                        }],
                    }]
                }
            }
        }
    })

    call_send_api(message_data)


def send_state_list(sender_id):
    message_data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "Select State",
                        "buttons": create_state_list(1)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(2)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(3)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(4)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(5)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(6)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(7)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(8)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(9)
                    }, {
                        "title": "Select State",
                        "buttons": create_state_list(10)
                    }]
                }
            }
        }
    })

    call_send_api(message_data)


def create_state_list(index):
    state_list = ["Maharashtra", "Kerala", "Karnataka", "Andhra Pradesh", "Tamil Nadu", "Delhi", "Uttar Pradesh",
                  "West Bengal", "Odisha", "Rajasthan", "Chhattisgarh", "Telangana", "Haryana", "Gujarat", "Bihar",
                  "Madhya Pradesh", "Assam", "Punjab", "Jharkhand", "Uttarakhand", "Himachal Pradesh", "Goa", "Tripura",
                  "Manipur", "Arunachal Pradesh", "Meghalaya", "Nagaland", "Sikkim", "Mizoram"]
    payload_list = []
    start_index = 0 + 3 * (index - 1)
    end_index = 29 if (start_index + 3) > 29 else (start_index + 3)
    for i in range(start_index, end_index):
        postback = {}
        postback["type"] = "postback"
        postback["title"] = state_list[i]
        postback["payload"] = state_list[i]
        payload_list.append(postback)
    return payload_list


def get_stats_send(sender_id, state):
    response = json.loads(requests.get(
        "https://api.covid19india.org/data.json").text)
    list_state = response['statewise']
    for i in list_state:
        if i['state'] == state:
            x = i
            break
    message_data = json.dumps({
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": "ACTIVE CASES: {}\nCONFIRMED CASES: {}\nDEATHS: {}\nRECOVERED: {}".format(x['active'],
                                                                                              x['confirmed'],
                                                                                              x['deaths'],
                                                                                              x['recovered'])
        }
    })
    call_send_api(message_data)


def process_postback(event):
    sender_id = event["sender"]["id"]
    payload = event["postback"]["payload"]

    if payload == C19INDIA:
        send_state_list(sender_id)
    else:
        get_stats_send(sender_id, payload)


def call_send_api(message_data):
    params = {
        "access_token":  ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }

    r = requests.post("https://graph.facebook.com/v5.0/me/messages",
                      params=params, headers=headers, data=message_data)


if __name__ == "__main__":
    app.run()
