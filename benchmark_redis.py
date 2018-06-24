from flask import Flask, session
from flask_session import Session

app = Flask(__name__)

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)


keys = list(range(0, 100000))


@app.route('/set/')
def set():
    key = keys.pop(0)
    session[key] = 'value'
    keys.append(key)
    return 'ok'

@app.route('/get/')
def get():
    key = keys.pop(0)
    value = session.get(key, 'not set')
    keys.append(key)
    return value

