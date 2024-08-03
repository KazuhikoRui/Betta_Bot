from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return 'Betta is a live...'

def run():
  app.run(host='0.0.0.0',port=8080)

def stay_a_live():
  t = Thread(target = run)
  t.start()