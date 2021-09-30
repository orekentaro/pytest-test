from flask import Flask, render_template

app = Flask(__name__)


@app.route('/greeting/<message>')
def sample(message):
  if message == 'bye':
    message = 'see you'
  elif message == 'unchi':
    message = 'buriburi'
  return message


@app.route('/top')
def top():
  return render_template('test.html')


# if __name__ == '__main__':
#   app.debug = True
#   app.run(host='127.0.0.1', port=5000)
