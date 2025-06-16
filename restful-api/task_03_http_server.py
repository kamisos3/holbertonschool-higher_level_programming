#!/usr/bin/python3
"""Module develops a simple API"""
import http.server
import socketserver
import json
import sys

PORT = 8000

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("Received GET request for:", self.path)

        if self.path == "/":
            response = "Hello, this is a simple API!"
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
            print(f"Serving at port {PORT}")
            print(f"Visit http://localhost:{PORT}")
            print("Press Ctrl+C to stop the server")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        print("Try changing the port of killing conflicting process", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("Server stopped by user")
