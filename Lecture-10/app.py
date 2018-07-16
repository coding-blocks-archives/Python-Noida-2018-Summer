from flask import Flask

from flask import request

from pymessenger.bot import Bot

bot = Bot("EAAC6j5edyf8BALZBMPOTZAYdSZAJUz5JZB7kHj69VuOZAx4S0OM2xvYwQ4DnKsNU3BYBaWX9vHdRgZBOqimI84e6oeT6KP63ALminJbGjJxeZCKvE6DosSU7YQPhZByaVZBMda0XM7elZCVlV5nI9nOIaGu1KR6ZBDHnZBHPXTfWbrGZABbR2MKyGPE8U")

app = Flask(__name__)


@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else :
        return "Please run it on facebook dev"


@app.route("/", methods=["POST"])
def message():

    data = request.get_json()

    print(data)

    if data.get("entry"):
        for entry in data["entry"]:
            if entry.get("messaging"):
                for message in entry["messaging"]:
                    if message.get('message'):
                        # Facebook Messenger ID for user so we know where to send response back to
                        user = message['sender']['id']
                        if message['message'].get('text'):
                            text = message['message']['text'] + " by bot"
                            bot.send_text_message(user, text)

                        if message['message'].get('attachments'):
                                for attachment in message['message']['attachments']:
                                    link = attachment['payload']['url']
                                    bot.send_image_url(user, link)


    return "Message recieved"
