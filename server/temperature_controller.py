from flask import request, jsonify
from services import set_comfort_temperature_service

def register_temperature_routes(app):
    @app.route('/set-comfort-temperature', methods=['POST'])
    def set_comfort_temperature():
        data = request.get_json()
        if data and 'temperature' in data:
            set_comfort_temperature_service(data['temperature'])
            return jsonify({"message": "Comfort temperature is set to " + str(data['temperature'])}), 200
        else:
            return jsonify({"error": "Error"}), 400
