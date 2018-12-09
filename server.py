from bottle import route, run, view, TEMPLATE_PATH
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

TEMPLATE_PATH.insert(0, './views')

@route("/")
@view('predictions')
def index():
  now = dt.now()

  x = random()


  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": [
      "После обеда ожидайте неожиданного праздника.",
      "Днём предостерегайтесь неожиданного праздника.",
      "Утром ожидайте гостей из забытого прошлого.",
    ],
    "special_date": x > 0.5,
    "x": x,
  }

@route("/api/forecasts")
def api_forecasts():
   return{"prophecies": generate_prophecies()}

run(
  host="localhost",
  port=8080,
  autoreload=True
)