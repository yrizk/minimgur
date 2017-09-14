import json
from flask import render_template

class ListAdapter():

	def __init__(self, jsonString):
		self.root = json.loads(jsonString);
		if (self.root['status'] is not 200 or self.root['success'] is not True):
			print('failure in network')
			raise MainFeedNetworkFailureException() # do I need to declare that I'm throwing this? also TODO: catch error in main.py and return error message
		else:
			self.data_list = []
			for item in self.root['data']:
				self.data_list.append(MinimgurItem(item))
				print('size: ' + str(len(self.data_list)))

	def render(self):
		return render_template('main.html', minimgur_list=self.data_list)

class MinimgurItem():

	def __init__(self, jsonObj):
		self.id = jsonObj['id']
		self.title = jsonObj['title']
		self.img = jsonObj['link']
