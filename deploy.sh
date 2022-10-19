poetry export -f requirements.txt --output requirements.txt
git add .
git commit -m "deploy to heroku"
# heroku login # 初回は必要,一度ログインしたら要らない
heroku git:remote -a jp-hacks-2022
# heroku側の環境変数を.envファイルをもとに設定, `heroku plugins:install heroku-config` が必要
heroku config:push --file=config/.env
git push heroku feat/LINEhook:main

echo https://jp-hacks-2022.herokuapp.com/