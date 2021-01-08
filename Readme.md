# Guide d'installation

## Download the project

`git clone https://github.com/xdanielsb/hackcloud.git`

`cd hackcloud`

## Install on your machine

### Backend

`cd logic`

`pip install -r ./requirements.txt`

`pip install tensorflow`

`export FLASK_APP=api.py`

`python -m flask run`

### Frontend

`cd view`

`npm install`

`npm run serve`

## Scalingo

Impossible: tensorflow is too large for our small server

## Test

http://localhost:8080 sur un navigateur
