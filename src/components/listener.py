from http.server import BaseHTTPRequestHandler
from json import loads

from src.components.ad_events_controller import AdEventsController


class Listener(BaseHTTPRequestHandler):
    def __init__(self, controller: AdEventsController, *args):
        self.controller = controller
        super().__init__(*args)

    def do_POST(self):
        try:
            event = loads(self.rfile.read(int(self.headers.get('Content-Length'))))
            print(event)
            self.controller.process_ad_event(event)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'OK')
        except Exception as err:
            print(err)