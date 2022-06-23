from pymavlink import mavutil
from flask import Flask, redirect, render_template, request, url_for, redirect

app = Flask(__name__)

the_connection = mavutil.mavlink_connection('udpin:localhost:14551')

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (the_connection.target_system, the_connection.target_component))

@app.route("/")
def home():
    while 1:
        msg1 = the_connection.recv_match(type='ATTITUDE', blocking=True)
        msg2 = the_connection.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        print(msg1)
        print(msg2)
        return render_template ("main.html", content1=msg1, content2=msg2)

if __name__ == '__main__':
    app.run(debug=True)