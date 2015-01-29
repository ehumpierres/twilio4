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

    response = twiml.Response()
    response.message(str(requestFormSid))


    TotalAmount = "55555"

    i = "title: Some title"
    j = "date: 2015-01-27"
    k = ""
    l = "test this crap"
	
    text_file = open("pages/pest.md", "w")

    text_file.write(str(i) + '\n')
    text_file.write(str(j) + '\n')
    text_file.write(str(k) + '\n')
    text_file.write("number I'm looking for %s" % TotalAmount)
	
    text_file.close()
 
    return str(response)

@app.route('/<path:path>/')
def page(path):
	return pages.get_or_404(path).html

if __name__ == '__main__':
	app.run(port=8000)