from flask import Flask, send_file, render_template, request, jsonify, send_from_directory
import json 
from datetime import datetime
import os 

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index2.html")

# @app.route('/<path:path>')
# def send_js(path):
#   return send_from_directory('templates/pedrotsividis.com/vgdl-games', path)

