from flask import Flask
import requests
from listadapter import ListAdapter
app = Flask(__name__)
 
CLIENT_ID = "5b0c23ba1e9064e"

@app.route("/")
def index():
	# TODO: if not logged in, rediret to login page
	r = requests.get("https://api.imgur.com/3/gallery/hot/viral/0/top", headers={"authorization": "Client-ID " + CLIENT_ID})
	listAdapter = ListAdapter(r.content)
	return listAdapter.render()
 
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