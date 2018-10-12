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



@app.route('/lex', methods=['GET', 'POST'])
def send_text():
	lex_response = lex.post_text(
	    botName='Cuora',
	    botAlias='dev',
	    userId='Test',
	    inputText= request.form['inputText']
	)
	if (lex_response["dialogState"] == "ReadyForFulfillment"):
		slots = lex_response["slots"]
		# If slots None, return general answer
		if (bool(slots) == False):
			# Return output directly 
			attributes = {"intentName": lex_response["intentName"]}
			output_response = API.getData(attributes)
			return output_response
		# Check if the Course key exist
		elif slots.get("Course") != None:
			slots["Course"] = getCourse(slots["Course"])
			if slots["Course"] == None:
				return ("Sorry, I did not understand you, what would you like me to do?")
			else:
				attributes = {"intentName": lex_response["intentName"], "slots": slots}
				output_response = API.getData(attributes)
				return output_response

		# Check if the Programme key exist
		elif slots.get("Programme") != None:
			attributes = {"intentName": lex_response["intentName"], "slots": slots}
			output_response = API.getData(attributes)
			return output_response
			
	else:
		return lex_response["message"]



# Called from the terminal
if __name__ == '__main__':
	app.debug = True # For development debugging not production
	app.run()