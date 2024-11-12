from thing import PiThing
from flask import *

#create flask app and pi thing
app = Flask(__name__)
pi_thing = PiThing()

@app.route("/")
def hello():
  return render_template('index.html', switch={})


@app.route("/led/<int:led_state>", methods=['POST'])
def led(led_state):
  if led_state == 0:
     pass
    #  pi_thing.set_led(False)
  elif led_state == 1:
     pass
    #  pi_thing.set_led(True)
  else:
     return ('Unknown LED State', 400)
  return (' ', 204)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)