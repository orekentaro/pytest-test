import pytest
from flask_mod import app


@pytest.fixture
def client():
  app.config['TESTING'] = True
  test_client = app.test_client()
  yield test_client
  test_client.delete()


def test_greeting_bye(client):
  result = client.get('/greeting/bye')
  assert b'see you' == result.data


def test_greeting_hello(client):
  result = client.get('/greeting/hello')
  assert b'hello' == result.data
