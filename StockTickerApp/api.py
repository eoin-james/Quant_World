from flask import Blueprint, request
from flask_restx import Api, Resource, fields
from models import db, TickerClass

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

ticker_model = api.model('TickerModel', {
    'DateTime': fields.String,
    'AAPL': fields.Float,
    'MSFT': fields.Float,
    'TEAM': fields.Float,
    'TSLA': fields.Float,
})


@api.route('/TickerClass')
class TickerClassDao(Resource):

    @api.marshal_with(ticker_model)
    def get(self, **kwargs):
        return TickerClass.query.all()

    @api.expect(ticker_model, validate=True)
    def post(self, **kwargs):
        data = request.json()
        row = TickerClass(**data)
        db.session.add(row)
        db.session.commit()
        return {"status": "success"}
