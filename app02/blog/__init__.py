from flask import Flask

app = Flask(__name__)

from app02.blog import routes
