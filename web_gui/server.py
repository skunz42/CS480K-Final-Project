from http.server import HTTPServer
from request_handler import RequestHandler

PORT = 8080

if __name__ == '__main__':
	try:
		server = HTTPServer(('localhost', 8080), RequestHandler)
		print('Starting server, use <Ctrl-C> to stop')
		server.serve_forever()
	except KeyboardInterrupt:
		print("Shutting Down.....")
		server.socket.close()