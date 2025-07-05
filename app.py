from os import path
from pathlib import Path
from flask import Flask, render_template
from flask_frozen import Freezer
import sys

DEBUG = True

template_folder = path.abspath('./wiki')
app = Flask(__name__, template_folder=template_folder)
app.config.from_object(__name__)

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/<page>' + '.html')
def render_page(page):
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')

# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8080)
