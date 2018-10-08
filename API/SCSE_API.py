from API.HelperFunctions.APIHelperFunctions import APIHelperFunctions
import json


class API():
	file = './API/CourseInfo.json'
	courseInfo = APIHelperFunctions.convertFileToJSON(file) # RESTful API is here
	# print(courseInfo)


	def getData(self, attributes):
		print(self.courseInfo["SCSE"]["Programme"][attributes["slots"]["Programme"]][attributes["slots"]["Year"]])
		# if attributes["intentName"] == "CourseByYearIntent":

		# 	# for course in self.coursei
		# 	print(courseInfo["SCSE"]["Programme"][attributes["slots"]["Programme"]][attributes["slots"]["Year"]])

	
# if __name__ == '__main__':
# 	newData = API()

	
