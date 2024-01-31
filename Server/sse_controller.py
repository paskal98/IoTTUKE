from flask import Response, stream_with_context
from mqtt_client import message_queue
import time
from flask_cors import CORS

def sse_stream():
    def event_stream():
        while True:
            if not message_queue.empty():
                message = message_queue.get()
                print(f"data: {message}\n\n")
                yield f"data: {message}\n\n"
            time.sleep(1)

    return stream_with_context(event_stream())

def register_sse_routes(app):
    CORS(app)
    @app.route('/events')
    def sse_request():
        return Response(sse_stream(), content_type='text/event-stream')
