import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
# load this environment's .env

app = Flask(__name__)
line_bot_api = LineBotApi("z+wwUFo23oaC1J9rxPOJY0cyFy7m0pB6ty6D2w077NVXKuVUpthMBTgQpCDQSZyMDF/WjPKHh9AdUHTxo2RutRulMIresZaPLGwN06VyxNVFX/fSjbucMnP0dgtsJnHFu2w/HaEPx3diJeCOJIXW+QdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("a676780a4132f1a41e5cab58d4b17674")
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/callback", methods=['POST'])
def callback():
  
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    app.run()
