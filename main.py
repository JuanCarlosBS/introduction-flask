from flask import Flask

app = Flask('flaskconftest')

@app.route('/')
def hello():
    return "Hello World!"

app.run()