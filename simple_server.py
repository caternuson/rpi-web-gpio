from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write("Hello Word".encode('ascii'))

server = HTTPServer(('', 8080), Handler)
server.serve_forever()
