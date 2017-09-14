import json
from flask import render_template

class ListAdapter():

	def __init__(self, jsonString):
		self.root = json.loads(jsonString);
		if (self.root['status'] is not 200 or self.root['success'] is not True):
			print('failure in network')
			raise NetworkException() # do I need to declare that I'm throwing this? also TODO: catch error in main.py and return error message
		else:
			self.data_list = []
			for x, item in enumerate(self.root['data']):
				if x > 30:
					break
				self.data_list.append(MinimgurItem(item))
			print('deserialization complete')

	def render(self):
		return render_template('main.html', minimgur_list=self.data_list)

class MinimgurItem():

	def __init__(self, jsonObj):
		self.id = jsonObj['id']
		self.title = jsonObj['title']
		self.img = jsonObj['link']


class NetworkError(SystemError):
	def __init__(self):
		pass

