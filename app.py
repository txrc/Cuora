import boto3
from flask import Flask, request, render_template


# AWS declaration of resources via boto3 #

# Get Lex Post methods
lex = boto3.client('lex-runtime', region_name='us-east-1') 

# End of AWS declaration of resources #


# To give our app a unique name __name__ is the string contains __main__ or __ or app 
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/lex')
def send_text():

	response = lex.post_text(
	    botName='mes_stx_seachat_bot',
	    botAlias='dev_intern',
	    userId='Test',
	    inputText='Hi, nice to meet you, I am Clement.'
	)
	print(response)
	return str(response)



# Called from the terminal
if __name__ == '__main__':
	app.debug = True # For development debugging not production
	app.run()