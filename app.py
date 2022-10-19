import datetime
import subprocess
import os
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

CONNECT_TIMEOUT,READ_TIMEOUT = 10,60*5
TIMEDIFF = 9
app = Flask(__name__)
line_bot_api = LineBotApi(os.environ["CHANNEL_ACCESS_TOKEN"],timeout=(CONNECT_TIMEOUT,READ_TIMEOUT))
handler = WebhookHandler(os.environ["CHANNEL_SECRET"])
print(f"Read timeout is {datetime.datetime.now() + datetime.timedelta(hours = TIMEDIFF,seconds=READ_TIMEOUT)}!!!")
@app.route("/")
def hello_world():
    return "<p>ohaohaoha, World!</p>"

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
    print(f"message text is '{event.message.text}'")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
