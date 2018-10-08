from API.SCSE_API import API
from flask import Flask, request, render_template
from getCourseCode import getCourse
import boto3, json


# AWS declaration of resources via boto3 #

# Get Lex Post methods
lex = boto3.client('lex-runtime', region_name='us-east-1') 

# End of AWS declaration of resources #

API = API()
# To give our app a unique name __name__ is the string contains __main__ or __ or app 
app = Flask(__name__)


@app.route('/')
def index():
	# render template if nothing is up
	return render_template('index.html')

@app.route('/newsevents')
def newsevents_page():
	return render_template('index.html')


@app.route('/gpaCalculator')
def gpaCalculator_page():
	return render_template('gpaCalculator.html')

@app.route('/faq')
def faq_page():
	return render_template('faqs.html')



@app.route('/lex')
def send_text():
	response = lex.post_text(
	    botName='Cuora',
	    botAlias='dev',
	    userId='Test',
	    inputText='Tell me about dete structures'
	)
	if (response["dialogState"] == "ReadyForFulfillment"):
		slots = response["slots"]
		if (slots == None):
			# Print output immediately 
			pass
		else:
			keyword = getCourse(slots["Course"])
			if (keyword != None):
				slots["Course"] = keyword
				attributes = {"intentName": response["intentName"], "slots": slots}
				output_response = API.getData(attributes)
				return json.dumps(output_response)
			else:
				return ("Sorry, I did not understand you, what would you like me to do?")


	else:
		return json.dumps(response["message"])



# Called from the terminal
if __name__ == '__main__':
	app.debug = True # For development debugging not production
	app.run()