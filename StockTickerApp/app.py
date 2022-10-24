import os
import time
from multiprocessing import Process
from flask import Flask, render_template

from api import blueprint
from login import uri
from models import db, TickerClass, LiveTickerClass
from data_loader import data_importer, test_load

"""
export FLASK_APP=StockTickerApp/app.py
export FLASK_DEBUG=1    
export FLASK_RUN_PORT=4444
flask run
"""

port = int(os.getenv('PORT', 4444))

# App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise app with extension
db.init_app(app)
with app.app_context():
    # Ensure all models are imported from other modules
    db.create_all()
app.register_blueprint(blueprint, url_prefix="/api")


@app.route('/')
def index():
    global p
    p = Process(target=parallel_data_load)
    p.start()
    return render_template('index.html')


@app.cli.command('load-data')
def load_data():
    db.create_all()

    test_load(db, TickerClass,
              'StockTickerApp/Data/test_data_2.csv',
              [str, float, float, float, float]
              )


def parallel_data_load():
    db.create_all()
    test_load(db, LiveTickerClass, 'StockTickerApp/Data/test_data_2.csv', [str, float, float, float, float])


if __name__ == '__main__':
    app.run(debug=True, port=port)
