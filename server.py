from wsgiref.simple_server import make_server

from hellp import application

httpd = make_server('', 8000, application)
print('serving HTTP on port 8000')
httpd.serve_forever()