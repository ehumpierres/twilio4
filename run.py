from flask import Flask, request, redirect
import twilio.twiml
 
SECRET_KEY = 'd634dffc544604661e8749d6328c413c'
app = Flask(__name__)
app.config.from_object(__name__)
 

@app.route("/", methods=['GET', 'POST'])
def getCookie():
    """Respond to incoming calls with a simple text message."""
 
    counter = session.get('counter', 0)
 
    # increment the counter
    counter += 1
 
    # Save the new counter value in the session
    session['counter'] = counter

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)



 
if __name__ == "__main__":
    app.run(debug=True)