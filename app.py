from flask import Flask

app = Flask(__name__)

# 動作確認用
@app.route('/')
def index():
    return 'Hello World.'

if __name__ == '__main__':
    app.run()
