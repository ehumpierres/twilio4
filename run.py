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

  content = """
     testeando
   """
  user = "Hero234"


  return render_template('output.html', **locals())
	
 
if __name__ == "__main__":
    app.debug = True
    app.run()



