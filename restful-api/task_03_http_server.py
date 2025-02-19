#!/usr/bin/python3
"""Python web server that handles different HTTP endpoints"""
import http.server
import socketserver
import json


# Define server port
PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler class
    Handles different endpoints with specific responses"""

    def do_GET(self):
        """Handle GET requests to different endpoints
        / : Returns welcome message
        """

        # Root endpoint - Welcome message
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Data endpoint - Returns JSON response
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(response_data).encode('utf-8'))

        # Status endpoint - Returns server status
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Handle 404 for undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


# Create HTTP server instance
Handler = MyHandler

# Start server and keep it running
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()  # Run server indefinitely
