import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import requests
import json

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Sample Data Model
class SampleData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Sample Data Schema
class SampleDataSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age')


# Aggregated Data Schema
class AggregatedDataSchema(ma.Schema):
    class Meta:
        fields = ('aggregated_age',)


sample_data_schema = SampleDataSchema()
sample_datas_schema = SampleDataSchema(many=True)
aggregated_data_schema = AggregatedDataSchema()


@app.route('/aggregate_data', methods=['GET'])
def aggregate_data():
    # Implement authentication and authorization here

    aggregated_age = db.session.query(db.func.sum(SampleData.age)).scalar()
    result = {'aggregated_age': aggregated_age}
    return aggregated_data_schema.jsonify(result)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
