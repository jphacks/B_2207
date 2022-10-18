poetry export -f requirements.txt --output requirements.txt
git add .
git commit -m "deploy to heroku"
heroku login
heroku git:remote -a jp-hacks-2022
git push heroku dev:main
