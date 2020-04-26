import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()