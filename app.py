from flask import Flask, send_file, render_template, request, jsonify, send_from_directory
import json 
from datetime import datetime
import os 
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
  # index2 is smooth looping of o.g. video 
  # index3 is random coords from send_coord 
  # index4 is mouse movement based
  return render_template("index4.html") 

@app.route('/coord')
def send_coord():
  return jsonify(random.random()) # replace this with [0, 1] value indicating tracked eye position, where 0 indicates left boundary and 1 indicates right