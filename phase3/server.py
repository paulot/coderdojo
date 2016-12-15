from http import server

server_address = ('0.0.0.0', 8000)
http_handler = server.SimpleHTTPRequestHandler
http_server = server.HTTPServer(server_address, handler)

try:
    http_server.serve_forever()
except KeyboardInterrupt:
    http_server.shutdown()
