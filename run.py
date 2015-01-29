from flask import Flask, request, make_response, session, render_template, url_for, redirect
from datetime import datetime, timedelta
from twilio import twiml
from twilio.rest import TwilioRestClient
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

counter = 0

@app.route('/',methods=['GET', 'POST'])
def index():


    requestFormSid = request.form.get('MessageSid')
    requestFormFrom = request.form.get('From')
    requestFormTo = request.form.get('To')
    requestFormBody = request.form.get('Body')

    response = twiml.Response()
    response.message(str(requestFormSid))

    #ToPrint = str(requestFormSid)

    i = "title: Some title"
    j = "date: 2015-01-27"
    k = ""
    
    text_file = open("pages/test.md", "w")

    text_file.write(str(i) + '\n')
    text_file.write(str(j) + '\n')
    text_file.write(str(k) + '\n')
    text_file.write("payload:: %s %s %s %s" % (requestFormSid, requestFormFrom, requestFormTo, requestFormBody))
	
    text_file.close()
 
    return str(response)

@app.route('/output/<path:test>')
def test(test):
    return pages.get_or_404(test).html


@app.route('/send/',methods=['GET', 'POST'])
def send():

    # Trotter's Account Sid and Auth Token from twilio.com/user/account
    account_sid = "AC1b3fcf6eb7ae41aa1c8f5dbf47cde6a9"
    auth_token  = "d634dffc544604661e8749d6328c413c"
    client = TwilioRestClient(account_sid, auth_token)
 
    message = client.messages.create(body="Probando 1,2,3..", to="+16178428225", from_="+16179345762")

    counter =+ 1

    return str("success: " + counter)
   

    

if __name__ == '__main__':
	app.run(port=8000)