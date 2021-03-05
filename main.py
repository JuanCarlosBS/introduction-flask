from flask import Flask

app = Flask('fascinates')


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/<beer>')
def pub(beer):
    return f'I prefer {beer}' 

app.run()
