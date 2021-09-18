from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os
import json, jsonify
client = MongoClient(os.environ['DB_HOST'])
db = client.test
 

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
@app.route("/user")
def userAdd():
    return render_template('AddUser.html')
@app.route("/db", methods=['GET','POST'])
def database():
#    client = MongoClient(os.environ['DB_HOST'])
#    db = client.test
    if request.method == 'POST':
        isim  = request.form.get('fname')
        soyad = request.form.get('lname')
        test = {
          'isim': isim,
          'soyad': soyad
        }
        result=db.users.insert_one(test)
    # return f'''
    # <h1>Kullanıcı Eklendi.{isim} --- {soyad}</h1>
    # '''
        return redirect(url_for('home'))

@app.route("/ulist")
def list():
    test = []
    coll = db['users']
    cursor = coll.find({})
    for i in cursor:
        test.append(i)
    return json.dumps(test)
