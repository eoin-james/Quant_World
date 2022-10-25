import os
from flask import Flask, render_template
from flask_executor import Executor

from api import blueprint
from login import uri
from models import db, TickerClass, LiveTickerClass
from data_loader import data_importer, test_load

from dev import market_state

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

executor = Executor(app)

# Initialise app with extension
db.init_app(app)
with app.app_context():
    # Ensure all models are imported from other modules
    db.create_all()
app.register_blueprint(blueprint, url_prefix="/api")


@app.route('/')
def index():
    if True:
        executor.submit(live_data_loader)
    return render_template('index.html')


@app.cli.command('load-data')
def load_data():
    db.create_all()

    test_load(db, LiveTickerClass,
              'StockTickerApp/Data/test_data_2.csv',
              [str, float, float, float, float]
              )


def live_data_loader():
    test_load(db, LiveTickerClass, 'Data/test_data_2.csv', [str, float, float, float, float])


def run_app():
    app.run(debug=True, port=port)


if __name__ == '__main__':
    run_app()

