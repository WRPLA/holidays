from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
metadata = Base.metadata

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/holidays.db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Holidays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    zone = db.Column(db.String(80))
    year_id = db.Column(db.ForeignKey('years.id'))
    country_id = db.Column(db.ForeignKey('countries.id'))

    year = db.relationship('Years')
    country = db.relationship('Countries')

    def __init__(self, name, start_date, end_date, zone, year_id, country_id):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.zone = zone
        self.year_id = year_id
        self.country_id = country_id


class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name


class Years(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    manager.run()