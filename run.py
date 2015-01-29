# FOR TWILIO we need at least to import twiml, TwilioRestClient, and Flask request
# FOR API instructions --> twilio.com AND https://twilio-python.readthedocs.org/en/latest/
from flask import Flask, request, make_response, session, render_template, url_for, redirect
from datetime import datetime, timedelta
from twilio import twiml
from twilio.rest import TwilioRestClient
from flask_flatpages import FlatPages


# We don't need this, I was using it to print to the browser
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)    # Not sure we need this, perhaps not
pages = FlatPages(app)              # We don't need this in production 

counter = 0

# IF WE WANT to change the URL with whiCH we receive Twilio sms
#   go to do it--> https://www.twilio.com/user/account/phone-numbers/incoming 
@app.route('/',methods=['GET', 'POST']) 
def index():

    # THIS CODE IS FOR RECEIVING AN SMS VIA A POST from the Twilio server acting as client
    # Read--> https://www.twilio.com/docs/api/twiml/sms/twilio_request for more parameters
    requestFormSid = request.form.get('MessageSid') # This is the unique identifier of the message
    requestFormFrom = request.form.get('From')      # This is the number that sent us the sms
    requestFormTo = request.form.get('To')          # This is the Twilio number we used to receive the sms
    requestFormBody = request.form.get('Body')      # This is the content of the sms that then needs to be parsed for urls

    # THIS TWILIO CODE is for replying back to a received message
    # Read--> https://www.twilio.com/docs/quickstart/python/sms/replying-to-sms-messages
    response = twiml.Response()
    response.message(str(requestFormSid))

    # THIS code is for exploring the cookies that Twilio sends and were conversations are tracked
    


    # The following code is for testing the variables received, using the browser
    i = "title: Some title"
    j = "date: 2015-01-27"
    k = ""
    
    text_file = open("pages/test.md", "w")

    text_file.write(str(i) + '\n')
    text_file.write(str(j) + '\n')
    text_file.write(str(k) + '\n')
    text_file.write("payload:: %s %s %s %s" % (requestFormSid, requestFormFrom, requestFormTo, requestFormBody))
	
    text_file.close()
    # END of the testing code
 
    return str(response)

# This code below is just for testing output via the browser
@app.route('/output/<path:test>')
def test(test):
    return pages.get_or_404(test).html
# END of testing code

# WITH THIS TWILIO CODE WE CAN SEND SMS TO ANY NUMBER
@app.route('/send/',methods=['GET', 'POST'])
def send():

    # Trotter's Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC1b3fcf6eb7ae41aa1c8f5dbf47cde6a9"
    auth_token  = "d634dffc544604661e8749d6328c413c"
    client = TwilioRestClient(account_sid, auth_token)
 
    # Here we generate the data necessary to send the sms
    payload =   "this is the message for the sms"
    recipient = "+16178428225"
    sender =    "+16179345762"

    # This code sends the sms, we can create all sorts of stuctures to handle and pass the parameters
    message = client.messages.create(body=payload, to=recipient, from_=sender)

    counter = counter + 1  # This is just for testing

    return str("success: " + str(counter)) 
   

    

if __name__ == '__main__':
	app.run(port=8000)