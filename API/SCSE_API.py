from API.HelperFunctions.APIHelperFunctions import APIHelperFunctions
import json


class API():
	file = './API/CourseInfo.json'
	courseInfo = APIHelperFunctions.convertFileToJSON(file) # RESTful API is here
	# print(courseInfo)


	def getData(self, attributes):
		if attributes["intentName"] == "CourseByYearIntent":
			for course in self.courseInfo["SCSE"]["Programme"][attributes["slots"]
				["Programme"]][attributes["slots"]["Year"]]:
				return self.courseInfo["SCSE"]["Programme"][attributes["slots"]
				["Programme"]][attributes["slots"]["Year"]][course]["CourseTitle"]

		elif attributes["intentName"] == "CourseIntent":
			info = self.getInfo(attributes["slots"]["Course"])
			return self.courseInfo["SCSE"]["Programme"][info[0]]["Year "+ info[1]][attributes["slots"]["Course"]]

	def getInfo(self, course):
		programme = course
		year = str(course[-4])
		if "CE/CZ" in programme:
			return ["CE/CZ", year]
		elif "CZ" in programme:
			return ["CZ", year]
		else:
			return ["CE", year]

	
# if __name__ == '__main__':
# 	newData = API()

	
