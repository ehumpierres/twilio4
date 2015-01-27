from flask import Flask, request, make_response, session
from datetime import datetime, timedelta
from twilio import twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
@app.route("/")
def sms():
 
    #get the cookie value, or default to zero
    #messagecount = int(request.cookies.get('messagecount',0))
    #messagecount += 1
 
    twml = twiml.Response.Message()

    #body = request.form['Body']
    #twml.sms("You've sent " + str(messagecount) + " messages in this conversation so far")
 
    #resp = make_response(str(body))
 
    #expires=datetime.utcnow() + timedelta(hours=4)
    #resp.set_cookie('messagecount',value=str(messagecount),expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))


 
    return str(twml)
 
if __name__ == "__main__":
    app.debug = True
    app.run()