from flask import Flask, jsonify

app = Flask('fascinates')


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/<beer>')
def pub(beer):
    return f'I prefer {beer}' 


@app.route('/user/<user_id>')
def user(user_id):
    user_content = {
        'user_id': user_id
    }

    return jsonify(user_content)
    

app.run()
