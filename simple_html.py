from http.server import HTTPServer, BaseHTTPRequestHandler

html = """
<html>
<body>
<h1>Hello World</h1>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(html))
        self.end_headers()
        self.wfile.write(html.encode('ascii'))

server = HTTPServer(('', 8000), Handler)
server.serve_forever()
