from flask import Flask, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

try:
	conn = MongoClient()
	print("connected")
except:
	print("not connected")

db = conn.database

collection = db.regstud

@app.route("/")
def home():
	return "Home"

@app.route("/insert")
def insert():
	collection.insert({"name" : "sana", "rollno": "16DCO49"},{"name":"afsha","rollno":"16DCO73"})
	return "inserted"

@app.route("/read")
def read():
	coll = collection.find({"name":"sana"})
	return coll[0]["name"]
app.run(debug = True)

