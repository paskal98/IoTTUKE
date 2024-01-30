from flask import Flask
from sse_controller import register_sse_routes

app = Flask(__name__)
register_sse_routes(app)
