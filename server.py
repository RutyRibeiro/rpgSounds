from flask import Flask, request
from models.Song import selectSong, createSong
from asyncio import run

app = Flask (__name__)

@app.route("/", methods =['GET'])
def index():
    return "Hello world!"

@app.route("/<path:id>", methods =['GET'])
def getSong(id):
    response = str(run(selectSong(id)))
    return response

@app.route("/", methods =['POST'])
def addSong():
    req = request.get_json()
    response = str(run(createSong(req['name'], req['link'], req['tags'], req['classification'])))
    return response

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)