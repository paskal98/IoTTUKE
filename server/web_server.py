from flask import Flask
from sse_controller import register_sse_routes
from temperature_controller import register_temperature_routes

app = Flask(__name__)

# Реєстрація SSE маршрутів
register_sse_routes(app)

# Реєстрація контролера температури
register_temperature_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
