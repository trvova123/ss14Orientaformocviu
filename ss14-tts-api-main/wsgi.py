from gevent.pywsgi import WSGIServer
from ss14tts import app

http_server = WSGIServer(("0.0.0.0", 5005), app)
http_server.serve_forever()