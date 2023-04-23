from flask import Flask, render_template, url_for, request, redirect
import sqlite3
from datetime import datetime, date, time
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # объект

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    color = db.Column(db.String(100))
    material_up = db.Column(db.String(100))
    material_down = db.Column(db.String(100))
    season = db.Column(db.String(100))
    sports = db.Column(db.String(100))
    size = db.Column(db.String(100))
    text = db.Column(db.Text)
    price = db.Column(db.Integer)

    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repl__(self):
        return '<Product %r> %self.id'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/about.html')  # отслеживание
def about():
    return render_template("about.html")  # "Aboutasdfasdf"


@app.route('/brands.html')  # отслеживание
def brands():
    return render_template("brands.html")  # "Aboutasdfasdf"


@app.route('/Nike.html')  # отслеживание
def Nike():
    return render_template("Nike.html")  # "Aboutasdfasdf"


@app.route('/Adidas.html')  # отслеживание
def Adidas():
    return render_template("Adidas.html")


@app.route('/NB.html')  # отслеживание
def NB():
    return render_template("NB.html")


@app.route('/header.html')  # отслеживание
def header():
    return render_template("header.html")


@app.route('/footer.html')  # отслеживание
def footer():
    return render_template("footer.html")


@app.route('/text.html')  # отслеживание
def text():
    return render_template("text.html")


@app.route('/store.html')  # отслеживание
def store():
    #запрос к дб сделать
    return render_template("store.html")


@app.route('/Main_sneck.html')  # отслеживание
def Main_sneck():
    return render_template("Main_sneck.html")


@app.route('/Main_sneck_adidas.html')  # отслеживание
def Main_sneck_adidas():
    return render_template("Main_sneck_adidas.html")


@app.route('/s.html')  # отслеживание
def s():
    return render_template("s.html")


if __name__ == '__main__':
    app.run(debug=True)  # команда запускает локальный сервер, ошибки выводятся на сайт
