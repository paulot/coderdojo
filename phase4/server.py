from http import server

server_address = ('0.0.0.0', 8000)
http_server = server.HTTPServer(server_address, server.SimpleHTTPRequestHandler)

try:
    http_server.serve_forever()
except KeyboardInterrupt:
    http_server.shutdown()
