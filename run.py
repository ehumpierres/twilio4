from flask import Flask, request, make_response, session, render_template, url_for, redirect
from datetime import datetime, timedelta
from twilio import twiml
from twilio.rest import TwilioRestClient
 
app = Flask(__name__)
 
@app.route("/",methods=['GET', 'POST'])
def sms():
 
    #get the cookie value, or default to zero
    #messagecount = int(request.cookies.get('messagecount',0))
    #messagecount += 1
 

    #requestArgs = request.args
    #print "requestArgs"
    #print requestArgs

    requestFormSid = request.form.get('Body')
   
    #requestFormFrom = 

    #requestData = request.data
    #print "requestData"
    #print requestData


    response = twiml.Response()
    response.message(str(requestFormSid))
    
    #twml.sms("You've sent " + str(messagecount) + " messages in this conversation so far")
 
    #resp = make_response(str(body))
 
    #expires=datetime.utcnow() + timedelta(hours=4)
    #resp.set_cookie('messagecount',value=str(messagecount),expires=expires.strftime('%a, %d %b %Y %H:%M:%S GMT'))

    #toPrint = "testing 123"
 
    return str(requestFormSid)
 
if __name__ == "__main__":
    app.debug = True
    app.run()