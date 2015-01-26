from flask import Flask, request, redirect, session
import twilio.twiml

# The session object makes use of a secret key.
SECRET_KEY = 'd634dffc544604661e8749d6328c413c'
app = Flask(__name__)
app.config.from_object(__name__)

# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+16178428225": "Ernesto",
}

@app.route("/", methods=['GET', 'POST'])
def getConvo():
    """Respond with the number of text messages sent between two parties."""
 
 	username = request.cookies.get('ernesto@gotrotter.com')

 
  	return username


 
if __name__ == "__main__":
    app.run(debug=True)