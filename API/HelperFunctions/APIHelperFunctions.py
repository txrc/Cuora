import json

class APIHelperFunctions():

	def convertFileToJSON(self, fileJSON):
		with open(fileJSON) as json_data:
			file = json.load(json_data)
			json_data.close()
		return file

	