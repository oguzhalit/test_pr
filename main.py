from flask import Flask, render_template
from pymongo import MongoClient
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
    client = MongoClient('mongodb+srv://root:myFirstDatabase@cluster0.cnu3s.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    db = client.test
    
    names = ['Oguz']
    company = ['Yok']
    
    test = {
      'name': names[0],
      'company': company[0]
    }
    
    result=db.reviews.insert_one(test)
    
    return f"Created {result.inserted_id}"
