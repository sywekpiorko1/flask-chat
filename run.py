import os
from flask import Flask, redirect

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """ Add messages to messages ist """
    messages.append("{}: {}".format(username, message))

def get_all_messages():
    """ Get all messages and separate using a 'br' tag """
    return "<br>".join(messages)

@app.route('/')
def index():
    """ Main page with instructions """
    return "To send a message use /USERNAME/MESSAGE"
    
@app.route('/<username>')
def user(username):
    """ Display chat messages """
    return "<h1>Welcome, {0}<h1>{1}".format(username, get_all_messages())
    
@app.route('/<username>/<message>')
def send_message(username, message):
    """ Create new message and redirect to the chat page """
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)