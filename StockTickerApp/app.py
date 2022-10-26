import os

from flask import Flask
from flask_executor import Executor


class AppClass:
    """
    This is an object wrapper for the Flask App - Since lots of Flask extensions are used this was designed to tidy up
    the app functionality
    """
    def __init__(self, blueprint, uri, db):

        self.blueprint = blueprint
        self.uri = uri
        self.db = db
        app, executor = self.setup()
        self.app = app
        self.executor = executor

    def setup(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = self.uri
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.executor = Executor(self.app)
        self.db.init_app(self.app)

        with self.app.app_context():
            # Ensure all models are imported from other modules
            self.db.create_all()
        self.app.register_blueprint(self.blueprint, url_prefix="/api")

        return self.app, self.executor

    def executor_submit(self, func, uri, tickers,  dt):
        return self.executor.submit(func, uri, tickers,  dt)

    def run(self, debug=True, port_num=4444):
        os_port_num = port = int(os.getenv('PORT', port_num))
        self.app.run(port=os_port_num, debug=debug)



