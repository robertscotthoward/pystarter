'''
Usage:
  From the command line, run::

    flask --app main.py --debug run

  This will start the Flask web but watch it for changes and automatically reload the site.
'''
import glob
import os
import re
import sys
import yaml

thisFile = os.path.abspath(__file__)
thisPath = os.path.dirname(thisFile)
root = os.path.abspath(os.path.join(thisPath, os.path.relpath('..')))
sys.path.insert(0, root)
sys.path.insert(0, os.path.join(root, 'src'))
paths = '\n  '.join(sys.path)

print(f"""
thisFile:  {thisFile}
thisPath:  {thisPath}
root:      {root}
sys.path:
{paths}
""")


import libs.tools as tools

from flask import Flask, Blueprint, render_template, request, send_file, redirect, send_from_directory
from api import *


site = Blueprint('PCA', __name__, template_folder='templates')
app = Flask(__name__)

app.register_blueprint(get_name)


@app.route('/')
def default():
  """The default route for the site.

  Returns:
      HTML: the resolved rendered template.
  """
  model = {
    'request': request
  }
  return render_template('main.html', model=model)


if __name__ == "__main__":
  app.run(host="0.0.0.0")
