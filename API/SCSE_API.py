import json

class API():


	def convertFileToJSON(self, fileJSON):
		with open(fileJSON) as json_data:
			file = json.load(json_data)
			json_data.close()

		return file

	def getData(self, attributes):
		path_to_api = self.convertFileToJSON("./API/CourseInfo.json")
		accessJson = attributes
		print(path_to_api)

		return json.dumps(attributes)



		# CHECK FOR COURSE NAME

		


if __name__ == '__main__':
	newData = API()
	data = newData.getData(attributes=None)
	# print(data)
	
