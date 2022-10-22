# サンプル（プロダクト名）

[![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2022/08/JPHACKS2022_ogp.jpg)](https://www.youtube.com/watch?v=LUPQFB4QyVo)

## 製品概要
「思い出から一つなぎのアートを」アップロードした画像から、一筆書きアートが浮かび上がるWebアプリ
### 背景(製品開発のきっかけ、課題等）
自分達の研究分野とプロダクトを繋げたい

→問題設定が分かりやすく、見せ方を工夫できるのはTSP（巡回セールスマン問題）だろう

→TSPを用いて何か別のアーティスティックな画像を生み出せたら面白いのではないか

こういった思考から画像からアートを生み出すTSPアートサービスを開発しました
### 製品説明（具体的な製品の説明）
### 特長
#### 1. 特長1　巡回セールスマン問題のためのアルゴリズムを今回の製品に取り入れた
今回は巡回セールスマン問題を解くための2-optというアルゴリズムを使い、画像からアートを浮かび上がらせることに成功した
#### 2. 特長2　アルゴリズムによってできた画像（完成品）だけでなく、どのように完成されたのかの過程も可視化することで待ち時間も楽しめる
画像から自動で頂点を生成し、巡回路が元の画像を浮かび上がらせるアートとなっていく過程がみれる


### 解決出来ること

画像からメッセージを面白く送信できる

### 今後の展望
動画・アニメーションに対応

指定したメッセージを表示できるようにする

2-optは解法としては遅いので、より高度なアルゴリズムを用いて高速に解けるようにする
### 注力したこと（こだわり等）
* TSPを解くためのアルゴリズム(2-opt)を組み込んだこと
* 

## 開発技術
### 活用した技術
#### API・データ
* 
* 

#### フレームワーク・ライブラリ・モジュール
* firebase
* Next.js
* OpenCV
#### デバイス


### 独自技術
#### ハッカソンで開発した独自機能・技術
* 
* 

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
* 巡回セールスマン問題に対するアルゴリズム
* 
