import json

class APIHelperFunctions():

	courseInfo = None

	def convertFileToJSON(self, file):
		with open(self.file, encoding="utf-8") as json_data:
			self.courseInfo = json.load(json_data)
			json_data.close()
		return courseInfo