# server.py
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer


class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, this is your localhost server.")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        decoded_data = post_data.decode('utf-8')
        json_data = json.loads(decoded_data)

        response_data = f"Received POST request with data: {json_data}"
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_data.encode('utf-8'))

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        decoded_data = put_data.decode('utf-8')
        json_data = json.loads(decoded_data)

        response_data = f"Received PUT request with data: {json_data}"
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(response_data.encode('utf-8'))


if __name__ == "__main__":
    server_address = ('localhost', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server is running at http://localhost:8000/")
    httpd.serve_forever()
