from http.server import BaseHTTPRequestHandler, HTTPServer
class HTTPHandler(BaseHTTPRequestHandler):
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
        arr = self.path.split('/')
        if arr[0] is "up":
          self.HTTPWrapper.up(arr[1])
        else:
          self.HTTPWrapper.right(arr[1])
        return
class HTTPWrapper:
  def __init__(self,Stepper1,Stepper2):
      self.Stepper1 = Stepper1
      self.Stepper2 = Stepper2
  def run(self):
      server_address = ('', 8081)
      self.httpd = HTTPServer(server_address, HTTPHandler)
      self.httpd.serve_forever()
  def stop(self):
      self.httpd.server_close()
  def up(x):
      self.Stepper1.currentW -= x/1000
  def right(y):
      self.Stepper2.currentW -= y/1000
