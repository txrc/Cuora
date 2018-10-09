from API.HelperFunctions.APIHelperFunctions import APIHelperFunctions
import json


class API():
	file = './API/CourseInfo.json'
	courseInfo = APIHelperFunctions.convertFileToJSON(file) # RESTful API is here
	# print(courseInfo)


	def getData(self, attributes):
		print(attributes)
		if attributes["intentName"] == "CourseByYearIntent":
			courseTitleString = ""
			for course in self.courseInfo["SCSE"]["Programme"][attributes["slots"]  \
					["Programme"]][attributes["slots"]["Year"]]:
					courseTitleString += (self.courseInfo["SCSE"]["Programme"][attributes["slots"] \
					["Programme"]][attributes["slots"]["Year"]][course]["CourseTitle"]) + "<br>"
			return "The courses you have to take are listed below: <br>" + courseTitleString

		elif attributes["intentName"] == "CourseIntent":
			info = self.getInfo(attributes["slots"]["Course"])
			course = self.courseInfo["SCSE"]["Programme"][info[0]]["Year " + info[1]]  \
				[attributes["slots"]["Course"]]
			return (course["CourseTitle"] + "<br> " + \
					 course["CourseAims"])

		elif attributes["intentName"] == "ProspectIntent":
			pass

		elif attributes["intentName"] == "assignmentIntent":
			pass

		elif attributes["intentName"] == "codingLanguageIntent":
			pass

		elif attributes["intentName"] == "coreGerpeIntent":
			pass

		elif attributes["intentName"] == "courseAssIntent":
			pass

		elif attributes["intentName"] == "courseSpecIntent":
			pass

		elif attributes["intentName"] == "creditIntent":
			print(attributes["slots"]["Course"])
			info = self.getInfo(attributes["slots"]["Course"])
			return self.courseInfo["SCSE"]["Programme"][info[0]]["Year " + info[1]]\
				[attributes["slots"]["Course"]]["AUs"]

		elif attributes["intentName"] == "DifferenceIntent":
			pass

		elif attributes["intentName"] == "gradCreditIntent":
			pass

		elif attributes["intentName"] == "priorIntent":
			pass

		elif attributes["intentName"] == "quizIntent":
			pass

		elif attributes["intentName"] == "specIntent":
			pass

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

	
