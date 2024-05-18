import sys
import logging

# Path to your project directory
sys.path.insert(0, "/home/cavegems/public_html/test.cavegems.space/my_flask_app")

from app import app as application

# Optional: Set up logging
logging.basicConfig(stream=sys.stderr)
