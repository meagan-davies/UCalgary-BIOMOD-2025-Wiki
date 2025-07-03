from os import path
from pathlib import Path

from flask import Flask, render_template
from flask_frozen import Freezer

import sys
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.html'

template_folder = path.abspath('./wiki')

app = Flask(__name__, template_folder=template_folder)

app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)


#app.config['FREEZER_BASE_URL'] = environ.get('CI_PAGES_URL')
app.config['FREEZER_DESTINATION'] = 'public'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)


# @app.cli.command()
# def freeze():
#     freezer.freeze()

# @app.cli.command()
# def serve():s
#     freezer.run()

@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/<page>')
def pages(page):
    return render_template(str(Path('pages')) + '/' + page.lower() + '.html')

# Main Function, Runs at http://0.0.0.0:8080
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8080)

