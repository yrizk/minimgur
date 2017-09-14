from flask import Flask, g, render_template
import requests
from listadapter import ListAdapter, NetworkError
app = Flask(__name__)
 
CLIENT_ID = "7dfb3564e49a8bd"
CLIENT_SECRET = "33dee0351d4543dbd49bdea44c461aa371c483ee"

MAIN_URL = "https://api.imgur.com/3/gallery/{0}/{1}/{2}/{3}"

@app.route("/", methods=['GET'])
def index():
	# TODO: if not logged in, redirect to login page
	r = requests.get(MAIN_URL.format("hot", "viral", "0", "top"), headers={"authorization": "Client-ID " + CLIENT_ID})
	try:
		listAdapter = ListAdapter(r.content)
		return listAdapter.render()
	except NetworkError:
		return "Problem with fetching imgur feed"
 
@app.route("/login", methods=['GET'])
# @templated('login.html') does not work :(
def login():
    return render_template('login.html', value="42")
  

if __name__ == "__main__":
    app.run()