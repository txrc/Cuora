from HelperFunctions.APIHelperFunctions import APIHelperFunctions
import json


class API():

	helper = APIHelperFunctions()
	courseInfo = helper.convertFileToJSON("../API/CourseInfo.json") # RESTful API is here


	def getData(self, attributes):
		print(self.courseInfo)
		return json.dumps(attributes)


if __name__ == '__main__':
	newData = API()

	
