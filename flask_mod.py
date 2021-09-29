from flask import Flask

app = Flask(__name__)


@app.route('/greeting/<message>')
def sample(message):
  if message == 'bye':
    message = 'see you'
  return message
