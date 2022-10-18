# 天気に関するAPIから体感温度を取得
# 実行する際はrootディレクトリから実行すること
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import json
from cmath import inf

import requests
from config.setting import Setting

## OpenWeatherMapというAPIを使うことにした
#API_TOKEN = "82b89b1719c61d4f68e481ab07d90feb" # OpenWeatherMapのAPIキー
API_TOKEN = Setting().wapi #環境変数を使う場合
#print(API_TOKEN)

# 体感気温の最低気温と最高気温の初期化
min_feels_tmps = inf
max_feels_tmps = -inf

tmp = [min_feels_tmps, max_feels_tmps] # 他に欲しい情報が出た時用に配列としてまとめて格納

def weatherInfo(place, tmp):
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
  ret = json.loads(response.text) # 今回のapiで得られる天気データをjson形式で受け取る
  # pprint.pprint(ret)
  today = ret["list"][0]["dt_txt"][5:10] # 今日の日付
  i = 0
  while ret["list"][i]["dt_txt"][5:10] == today: # 取得したデータが今日の日付である場合に最低・最高気温を比較して更新
    if tmp[0] > float(ret["list"][i]["main"]["feels_like"]):
      tmp[0] = ret["list"][i]["main"]["feels_like"]
    if tmp[1] < float(ret["list"][i]["main"]["feels_like"]):
      tmp[1] = ret["list"][i]["main"]["feels_like"]
    i += 1

def getMinFeelTmp(): # 体感気温の最低気温を取得
  return tmp[0]

def getMaxFeelTmp(): # 体感気温の最高気温を取得
  return tmp[1]


# テストコード 
# place = str(input()) #都道府県を入力
# weatherInfo(place, tmp)
# print(getMinFeelTmp())
# print(getMaxFeelTmp())
    


