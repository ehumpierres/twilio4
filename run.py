from flask import Flask, request, redirect, session
import twilio.twiml
 
SECRET_KEY = 'd634dffc544604661e8749d6328c413c'
app = Flask(__name__)
app.config.from_object(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def getCookie():
    """Respond to incoming calls with a simple text message."""
 
    
	convo = request.cookies()   
  
    message = "Hello, Mobile Monkey"

    resp = twilio.twiml.Response()
    resp.sms(message)
    return str(convo)




 
if __name__ == "__main__":
    app.run(debug=True)