#!/usr/bin/env python

import sys
import logging
from flup.server.fcgi import WSGIServer

# Add the directory containing your Flask app to the PYTHONPATH
sys.path.insert(0, "/home/cavegems/public_html/test.cavegems.space/my_flask_app.PI")

# Import your Flask app
from app import app

# Optional: Set up logging
logging.basicConfig(stream=sys.stderr)

# Run the WSGI server using FastCGI
if __name__ == '__main__':
    WSGIServer(app).run()
