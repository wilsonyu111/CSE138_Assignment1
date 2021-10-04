from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json

app = Flask(__name__)

@app.route('/hello', methods=['GET']) # default home page
def hello():

        return json.dumps({"message" : "world"}), 200

@app.route ('/hello/<name>', methods=['POST'])
def hello_post(name = None):
        
        if name == None:
                return "Not allowed", 405
        else:
                return json.dumps({"message" : "Hi, " + name +"."}), 200

@app.route ('/hello/<name>', methods=['GET'])
def hello_post_bad(name):
         
        return "Method Not Allowed", 405

@app.route ("/test", methods=['GET'])
def test():
        return json.dumps({"message":"test is successful"})

@app.route ("/test/<msg>", methods=['POST'])
def test_post(msg):
        
        return json.dumps({"message" : msg}), 200
        

@app.route ("/test", methods=['POST'])
def test_bad():
        
        val = request.args.get("msg")
        if val:
                return json.dumps({"message": val})
        else:
                return "Bad Request", 400
        
if __name__ == "__main__": # in order to run it as main, it needs to be ran as python "file_name"

        
	app.run(debug=True, host= '0.0.0.0', port= "8090") #allow the server to run in debug mode without setting it in console

