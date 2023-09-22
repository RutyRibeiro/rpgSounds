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
    name = request.get_json()['name']
    link = request.get_json()['link']
    tags = request.get_json()['tags']
    classification = request.get_json()['classification']
    response = str(run(createSong(name, link, tags, classification)))
    return response

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)