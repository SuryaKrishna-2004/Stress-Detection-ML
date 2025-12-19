
from flask import *
from public import public
from admin import admin
from health import health
from staff import staff
from flask_mail import Mail
import smtplib
from email.mime.text import MIMEText 
from api import api

app = Flask(__name__)
app.secret_key = "key"

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(health)
app.register_blueprint(staff)
app.register_blueprint(api,url_prefix='/api')


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'lbetter24x7@gmail.com'
app.config['MAIL_PASSWORD'] = 'jjwrgcahofexprck'
app.config['MAIL_USE_TLS'] = False        
app.config['MAIL_USE_SSL'] = True



app.run(debug=True,port=5050,host="0.0.0.0")

