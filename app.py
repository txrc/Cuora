from API.SCSE_API import API
from flask import Flask, request, render_template
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

@app.route('/lex')
def send_text():
	response = lex.post_text(
	    botName='Cuora',
	    botAlias='dev',
	    userId='Test',
	    inputText='In year 3 what course do we have to take for CS'
	)
	if (response["dialogState"] == "ReadyForFulfillment"):
		attributes = {"intentName": response["intentName"], "slots": response["slots"]} 
		output_response = API.getData(attributes)
		return output_response
	else:
		return json.dumps(response["message"])



# Called from the terminal
if __name__ == '__main__':
	app.debug = True # For development debugging not production
	app.run()