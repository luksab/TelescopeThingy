from http.server import BaseHTTPRequestHandler, HTTPServer
class HTTPHandler(BaseHTTPRequestHandler):
  def __init__(self,Stepper1,Stepper2):
      self.Stepper1 = Stepper1
      self.Stepper2 = Stepper2
  def run(self):
      server_address = ('', 8081)
      httpd = HTTPServer(server_address, HTTPHandler)
      httpd.serve_forever()
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
