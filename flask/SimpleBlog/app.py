from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dtm

import sys as system
system.path.append('utils')
#print(system.path)

import urlList as routing

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=dtm.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id



@app.route(routing.MAIN_URL1)
@app.route(routing.MAIN_URL2)
def index():
    return render_template("index.html")


@app.route(routing.ABOUT_URL)
def about():
    return render_template("about.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User " + name + " " + str(id)


@app.route(routing.NEW_URL, methods=['POST', 'GET'])
def create():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Article(
            title=title,
            intro=intro,
            text=text
        )

        try:
            db.session.add(article)
            db.session.commit()
            return redirect(routing.MAIN_URL1)
        except:
            return "Error"
        finally:
            print("Article " + title + " got")
    else:
        return render_template("create-new-article.html")


@app.route(routing.ARTICLES_URL)
def show():
    return render_template("articles.html")


if __name__ == "__main__":
    app.run(debug=True)
