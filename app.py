from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<username>')
def show_user_profile(username):
    return "username: {0}".format(username)

@app.route('/about')
def about():
    return "about page"

@app.route('/projects/')
def projects():
    return "project page"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)
