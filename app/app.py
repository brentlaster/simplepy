from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from werkzeug.exceptions import HTTPException
import socket

app = Flask(__name__)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
fqdn = socket.getfqdn()
print (fqdn)
host_id = host_ip if host_name.isalnum() else fqdn

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        error_code = e.code
        error_str = str(e)
    return render_template("error.html", error=error_str, code=error_code)


@app.route('/')
def home():
    return render_template("index.html", message="Hello!", host=host_id)

@app.route('/userpage/<user>')
def user_home(user):
   return render_template("user_home.html", message="Welcome {}".format(user), host=host_id)

@app.route('/login',methods = ['POST', 'GET'])
def user_login():
   if request.method == 'POST':
      id = request.form['user_name']
      return redirect(url_for('user_home',user = id))
   else:
      id = request.args.get('user_name')
      return render_template('user_login.html', host
=host_id)


if __name__ == '__main__':
   app.run(host=host_ip, port=8080)
