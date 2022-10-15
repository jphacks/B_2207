# サービス名

## 環境と各ディレクトリ・ファイルの役割

### パッケージ管理

LINE Bot の作成にあたって，パッケージ管理は Poetry を使用する． Poetry は Java における Maven のような役割を果たす Python のパッケージ管理ツールである．今回は Poetry を使って，メンバー間の環境に差がでないようにする．

### LINE API との連携

LINE のメッセージがユーザから送信されると， Flask(Web API を作るためのフレームワーク) で記述された API が呼ばれて，ユーザが送信した画像を取得して処理をした上で DB に登録する等が可能となる．Flask の API は`app.js`に記述されている．

### 定期実行

また，API とは別に定期実行に関する処理を管理する`periodic_processing`というディレクトリを作成している．`search_coordinations.py`では天候に合う服の組み合わせを各ユーザに対して探す処理を記述し，`send_coordinations.py`では見つけた服の組み合わせを各ユーザの LINE に送る処理を行う．`search_coordinations.py`は実行に時間がかかることが想定されるため，`search_coordinations.py`実行後，十分な時間を開けて`send_coordinations.py`を実行することにする（将来的にはこの実装は改善したほうが良い）．

### その他のディレクトリの役割

config，model，notebooks，data および recommender は LINE API との連携でも，定期実行でも共通して利用する．

- config：API のアクセストークンや Firebase の設定等を管理するためのディレクトリ
- model：DB の IO 処理を管理するためのディレクトリ
- notebooks：手法を研究するために使う jupyter notebooks を格納するためのディレクトリ
- data：服装の学習データを格納する用のディレクトリ
- recommender：ユーザに服装の組み合わせを勧めるための処理をまとめたディレクトリ

## 環境構築

### 環境変数等の設定

Slack から`.env`と`.jphacks-2022-firebase-adminsdk-ijn6v-e2108c052f.json`をコピーして，`config`配下にコピーする．

### Poetry のインストール

まず，以下の記事を参考に Poetry のインストールを行ってほしい．なお，環境は既に作ってあるので，環境を作る部分は行う必要はない．

https://qiita.com/sabaku20XX/items/6147432996fccc335568

### パッケージのインストールとインタプリタの設定

```
poetry install
```

次に以下の手順で VSCode の環境に Poetry の仮想環境を認識させる．

1. app.py を開く
2. 右下の Python のバージョンが書かれている部分をクリック
3. 「インタプリタのパスを入力」をクリック
4. `./.venv/bin/python`を入力して決定

ここまで完了したら，`./app.py`で右上の ▶ をクリックして実行し，`http://127.0.0.1:5000`を開き，`Hello World.`が出力されていることを確かめる．確認が正しく出来たら，環境設定は完了である．

### Python のパッケージを追加したい場合

以下のコマンドを使ってパッケージを追加することができる．pip は使わないことに注意．

```
poetry add <package-name>
例：poetry add numpy
```

### Poetry 上でコマンドを実行する場合

以下の形式で Poetry 上の環境でコマンドを実行することができる．

```
poetry run <command>
例：poetry run jupyter notebook
```

# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要

### 背景(製品開発のきっかけ、課題等）

### 製品説明（具体的な製品の説明）

### 特長

#### 1. 特長 1

#### 2. 特長 2

#### 3. 特長 3

### 解決出来ること

### 今後の展望

### 注力したこと（こだわり等）

-
-

## 開発技術

### 活用した技術

#### API・データ

-
-

#### フレームワーク・ライブラリ・モジュール

-
-

#### デバイス

-
-

### 独自技術

#### ハッカソンで開発した独自機能・技術

- 独自で開発したものの内容をこちらに記載してください
- 特に力を入れた部分をファイルリンク、または commit_id を記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）

-
-
