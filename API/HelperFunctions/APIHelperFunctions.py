import json

class APIHelperFunctions():

	courseInfo = None

	def convertFileToJSON(file):
		with open(file) as json_data:
			courseInfo = json.load(json_data)
			json_data.close()
		return courseInfo
