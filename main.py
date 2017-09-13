from flask import Flask
import requests
app = Flask(__name__)
 
CLIENT_ID = "5b0c23ba1e9064e"

@app.route("/")
def index():
	r = requests.get("https://api.imgur.com/3/gallery/hot/viral/0/top", headers={"authorization": "Client-ID " + CLIENT_ID})
	return r.content
 
@app.route("/hello")
def hello():
    return "Hello World!"
 
@app.route("/members")
def members():
    return "Members"
 
@app.route("/members/<string:name>/")
def getMember(name):
    return name
 
if __name__ == "__main__":
    app.run()