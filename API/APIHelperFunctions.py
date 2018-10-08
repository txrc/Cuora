import json

class APIHelperFunctions():

	courseInfo = None

	def convertFileToJSON(self, file):
		with open(self.file) as json_data:
			courseInfo = json.load(json_data)
			json_data.close()
		return courseInfo
