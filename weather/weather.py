# 天気に関するAPIから体感温度を取得

import json
from cmath import inf

import requests

## OpenWeatherMapというAPIを使うことにした
API_TOKEN = "82b89b1719c61d4f68e481ab07d90feb" # OpenWeatherMapのAPIキー


place = str(input()) # 暫定として47都道府県をターミナルで入力する形を取った
if place == "大阪" or place == "京都":
  place += "府"
elif place == "東京":
  place += "都"
elif place == "北海道": # 北海道だけは「北海道」と入力されるだろうと想定
  pass
else:
  place += "県"
    
response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast", #3時間ごと５日間の天気情報を得られる
params={
    ## 緯度・軽度を指定する場合
    # "lat": "35.68944",
    # "lon": "139.69167",

    ## 都市名で取得する場合
    "q": place,

    "appid": API_TOKEN, # APIキーを指定
    "units": "metric",  #温度を摂氏で取得
    "lang": "ja", # 日本語表記
  },
)
ret = json.loads(response.text) # 今回のapiで得られる天気データがjson形式で受け取る
# pprint.pprint(ret)
min_feel_tmps = inf # 体感気温の最低値の初期化
today = ret["list"][0]["dt_txt"][5:10] # 今日の日付
i = 0
while ret["list"][i]["dt_txt"][5:10] == today: # 取得したデータが今日の日付である場合に最低気温を比較して更新
  if min_feel_tmps > float(ret["list"][i]["main"]["feels_like"]):
    min_feel_tmps = ret["list"][i]["main"]["feels_like"]
  i += 1
#print(min_feel_tmps)
    
