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

#@app.route('/<path:path>/')
@app.route('/test')
def test(path):
	return pages.get_or_404(path).html


#@app.route('/',methods=['GET', 'POST'])
#def sendSMS():






if __name__ == '__main__':
	app.run(port=8000)