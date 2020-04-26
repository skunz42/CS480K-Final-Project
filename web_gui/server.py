import http.server
import cgi

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path=="/":
			self.path="/index.html"

		return http.server.SimpleHTTPRequestHandler.do_GET(self)

	def do_PUT(self):
		if self.path=="/send":
			form = cgi.FieldStorage(
				fp=self.rfile, 
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'],
			})

			print ("City Name: %s" % form["city_name"].value)
			print ("State Abreviation: " % form["state_abrv"].value)
			self.send_response(200)
			self.end_headers()
			self.wfile.write("Searching: " + form["city_name"].value + ", " + form["state_abrv"].value + "!")
			return	

#Temporary replace later once custom handler is working
#TmpHandler = http.server.SimpleHTTPRequestHandler

if __name__ == '__main__':
	from http.server import HTTPServer
	try:
		server = HTTPServer(('localhost', 8080), Handler)
		print('Starting server, use <Ctrl-C> to stop')
		server.serve_forever()
	except KeyboardInterrupt:
		print("Shutting Down.....")
		server.socket.close()