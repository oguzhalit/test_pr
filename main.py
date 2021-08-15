from flask import Flask, render_template
from pymongo import MongoClient
import os
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route("/db")
def database():

    client = MongoClient(os.environ['DB_HOST'])
    db = client.test

    names = ['Miyav']
    company = ['Kedi']

    test = {
      'name': names[0],
      'company': company[0]
    }

    result=db.reviews.insert_one(test)

    return f"Created {result.inserted_id}"
