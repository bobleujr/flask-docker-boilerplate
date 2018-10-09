from flask import Flask
from app.main.controllers import main
from app.login.controllers import login

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/main')
app.register_blueprint(login, url_prefix='/login')