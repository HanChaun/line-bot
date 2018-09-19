from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('+s3zHD/JLHUwYQ96oYEio2GD/kVtScINqt3QDvOf9VzzFTycaNoMfJcDZ55jQ6lTrq9isWhGqY0cG+g0LCkpa0QyFPxCufLNXAmWpBWNpHfgtx03Sqi6K3fKouORwwBoJHvlz2WeqaxQ6yJveZjmaQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('5f1c3b9497741fa8deb59ccbdd7e4ce3')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '我看不懂你說什麼'

    if msg in ['Hi','hi']:
        r = 'hi'
    elif msg == '你吃飯了嗎?' :
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
         r = '你想訂位 是嘛?'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()