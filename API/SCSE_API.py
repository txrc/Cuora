from API.HelperFunctions.APIHelperFunctions import APIHelperFunctions
import json

class API():
	file = './API/CourseInfo.json'
	# test = APIHelperFunctions()
	courseInfo = APIHelperFunctions.convertFileToJSON(file) # RESTful API is here
	# print(courseInfo)


	def getData(self, attributes):
		# print(attributes)
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

		elif attributes["intentName"] == "ProspectsIntent":
			return ("Overall Employment rate for CS: 92.4% Mean Salary for CS students: $3,667 <br>\
					Overall Employment rate for CE: 95.1% Mean Salary for CE students: $4,078 <br>\
					For more information visit: <br>\
					<a href='http://scse.ntu.edu.sg/Programmes/ProspectiveStudents/Undergraduate/Documents/GESntu.pdf'>SCSE Prospects</a> \
					")

		elif attributes["intentName"] == "codingLanguageIntent":
			return ("There isn\'t a requirement on the coding language you use in most courses in SCSE. However, some of the key courses that require you to know the particular language are listed below: <br> \
				CE/CZ1003: Introduction to Computational Thinking: Python Programming <br> \
				CE/CZ1007: Data Structures: C Programming <br> \
				CE/CZ2002: Object Oriented Design & Programming: Java Programming <br> \
				")

		elif attributes["intentName"] == "coreGerpeIntent":
			return ("Core modules are mandatory for you to take before you can graduate, whereas Major Prescribed Electives are Year 4 specialization modules.")


		elif attributes["intentName"] == "courseSpecIntent":
			return ("There are total of 31 CE/CZ specialization courses. Both CS and CE courses share the specialization courses. You can check out the CE/CZ specialization courses individually by typing the course name or the course code. tudents have to choose at least 5 elective courses from any of the below specialization focus areas: <br>\
					<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Documents/2018/CE/4.%20EF%20for%20Artificial%20Intelligence.pdf' target='_blank'>Artificial Intelligence</a><br>\
					<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Documents/2018/CE/5.%20EF%20for%20Cyber%20Physical%20Systems.pdf' target='_blank'>Cyber Physical Systems</a><br>\
					<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Documents/2018/CE/6.%20EF%20for%20Cyber%20Security.pdf' target='_blank'>Cyber Security</a><br>\
					<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Documents/2018/CE/7.%20EF%20for%20Data%20Science%20n%20Analytics.pdf' target='_blank'>Data Science & Analytics</a><br>\
					<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Documents/2018/CE/2.%20EF%20for%20High%20Performance%20Computing.pdf' target='_blank'>High Performance Computing</a><br>\
					<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Documents/2018/CE/3.%20EF%20for%20Networking%20n%20Mobility.pdf' target='_blank'>Networking & Mobility</a><br>\
					For more information, click on the respective focus area to see what modules are being offered. A student must read at least 3 elective courses from the respective focus area to gain the elective focus on that particular area. \
					")

		elif attributes["intentName"] == "creditIntent":
			info = self.getInfo(attributes["slots"]["Course"])
			AU = self.courseInfo["SCSE"]["Programme"][info[0]]["Year " + info[1]][attributes["slots"]["Course"]]["AUs"]
			return ("The number of credit AUs for this course is " + str(AU))

		elif attributes["intentName"] == "DifferenceIntent":
			return ("Most of the CS / CE students share this opinion, Computer Science usually focuses on the coding \
				aspect of things, focusing on exclusive topics like 'CZ2007 - Introduction to Databases' which focuses on clients, servers, operating systems, \
				whereas Computer Engineering has exclusive topics like 'CE2004 - Circuits and Signal Analysis' which focuses on understanding the hardware. ")

		elif attributes["intentName"] == "gradCreditIntent":
			return ("The total amount of AUs needed to graduate for JC/Poly students amounts to 140 AUs. For JC students, they have to complete the course of study within 4 years along with a professional internship (PI). For Poly students, they have an option to complete the course within 3 or 3.5 years along with the professional internship as well and as poly students are exempted, they only need to do 110 AUs with a total of 30 AUs credited upon entering the course. For more information visit: \
						<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Pages/CS.aspx' target='_blank'>Computer Science</a><br> \
						<a href='http://scse.ntu.edu.sg/Programmes/CurrentStudents/Undergraduate/Pages/CE.aspx' target='_blank'>Computer Engineering</a><br> \
						")

		elif attributes["intentName"] == "priorIntent":
			return ("Most of the course content involves Mathematics and Programming. Basic Programming skills is good enough to have an overview of the entire course. Throughout the course you will learn advance techniques and methodologies to refactor your code. As for Mathematics, if you have not done Calculus before. You may have slight difficulties with coping. \
					Some of the websites that will help you throughout your studies are listed below: <br>\
					<a href='https://www.khanacademy.org/	' target='_blank'>Khan Academy</a><br> \
					<a href='https://www.coursera.org/' target='_blank'>Coursera</a><br> \
					")

		elif attributes["intentName"] == "quizIntent":
			info = self.getInfo(attributes["slots"]["Course"])
			assessment = self.courseInfo["SCSE"]["Programme"][info[0]]["Year " + info[1]][attributes["slots"]["Course"]]["Assessment"]
			return ("The list of assessments are as follows: " + assessment)

		elif attributes["intentName"] == "GreetingIntent":
			return ("Hi, nice to meet you, I am Cuora. I can answer most SCSE related questions. Prospects, Infomration about Courses.")

	def getInfo(self, course):
		programme = course
		year = str(course[-4])
		if "CE/CZ" in programme:
			return ["CE/CZ", year]
		elif "CZ" in programme:
			return ["CZ", year]
		else:
			return ["CE", year]

	
if __name__ == '__main__':
	newData	

	
