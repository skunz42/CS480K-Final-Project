import http.server

PORT = 8080

class Handler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		pass

	def do_PUT(self):
		pass

#Temporary replace later once custom handler is working
TmpHandler = http.server.SimpleHTTPRequestHandler

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), TmpHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()