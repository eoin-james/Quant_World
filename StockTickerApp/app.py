import os
from flask import Flask, render_template

from api import blueprint
from login import uri
from models import db, TickerClass
from data_loader import data_importer

# App
app = Flask(__name__)

# Configure database
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
    return render_template('index.html')


@app.cli.command('load-data')
def load_data():
    db.create_all()

    data_importer(db, TickerClass,
                  'StockTickerApp/Data/test_data_2.csv',
                  [str, float, float, float, float]
                  )


if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv('PORT', 4444)))
    """
    export FLASK_APP=StockTickerApp/app.py
    export FLASK_DEBUG=1    
    export FLASK_RUN_PORT=4444
    flask run
    """
