from flask import Flask, jsonify, render_template

app = Flask('fascinates', template_folder='./static')


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


@app.route('/render/<ano>')
def template(ano):
    return render_template(
        './teste.html',
        ano=ano,
    )

app.run()
