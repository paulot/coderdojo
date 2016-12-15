import SimpleHTTPServer
import SocketServer

address = ('0.0.0.0', 8000)
handler = SimpleHTTPServer.SimpleHTTPRequestHandler

server = SocketServer.TCPServer(address, handler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    server.shutdown()
