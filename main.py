from flask import Flask,url_for,render_template,redirect

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return render_template("home.html",stuff=name,age = ,height = ) #input your name,age and height 


if __name__ == '__main__':
    app.run()
