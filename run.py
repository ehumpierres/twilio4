from flask import Flask, request, make_response, session, render_template, url_for, redirect
from datetime import datetime, timedelta
from twilio import twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
@app.route("/",methods=['GET', 'POST'])
def sms():
 

    requestFormSid = request.form.get('MessageSid')

    response = twiml.Response()
    response.message(str(requestFormSid))
    
    return str(response)


@app.route("/output",methods=['GET', 'POST'])
def output():

	f = open('index.html','w')

    output = """ <html>
			<head>
 				<title>Feature information</title>
			</head>
			<body>
				<p>This is a test</p>
			</body>
		</html> """

	f.write(output)
	f.close()

	return render_template('index.html')	

	
 
if __name__ == "__main__":
    app.debug = True
    app.run()



#@app.route("/",methods=['POST'])

