import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore


class Setting:
    def __init__(self):
        # .envから環境変数を読み込む
        load_dotenv("./config/.env")

        # Firebaseから設定値を取得
        cred = credentials.Certificate("./config/jphacks-2022-firebase-adminsdk-ijn6v-e2108c052f.json")
        firebase_admin.initialize_app(cred)
        self.__db = firestore.client()

        # 環境変数から設定値を取得
        # .envに環境変数を追加した場合はSlackで全メンバーに伝えること
        # 以下のhogeのように環境変数を取得する
        # self.__hoge = os.environ.get("HOGE")

    @property
    def db(self):
        return self.__db

    # 環境変数を追加したらpropertyにも追加すること
    # これによりsettingで参照できるようになる
    # @property
    # def hoge(self):
    #     return self.__hoge
