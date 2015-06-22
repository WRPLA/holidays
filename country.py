__author__ = 'baptiste'
from scholarholidays import *
session = db.session()
import datetime


class France:

    def __init__(self):
        self.name = 'France'

    def is_holiday(self, date):
        res = db.session.query(Holidays).filter(Countries.name == self.name,
                                                Countries.id == Holidays.country_id,
                                                Holidays.start_date <= date,
                                                Holidays.end_date >= date)\
            .all()
        if len(res) == 0:
            print('no holidays')
            return False
        else:
            return True

    def get_zones(self, date):
        res = db.session.query(Holidays.zone).filter(Countries.name == self.name,
                                                     Countries.id == Holidays.country_id,
                                                     Holidays.start_date <= date,
                                                     Holidays.end_date >= date,
                                                     Holidays.zone != self.name)\
            .all()
        return res


class Germany:

    def __init__(self):
        self.name = 'Germany'

    def is_holiday(self, date):
        res = db.session.query(Holidays).filter(Countries.name == self.name,
                                                Countries.id == Holidays.country_id,
                                                Holidays.start_date <= date,
                                                Holidays.end_date >= date)\
            .all()
        if len(res) == 0:
            print('no holidays')
            return False
        else:
            return True


class UK:

    def __init__(self):
        self.name = 'UK'

    def is_holiday(self, date):
        res = db.session.query(Holidays).filter(Countries.name == self.name,
                                                Countries.id == Holidays.country_id,
                                                Holidays.start_date <= date,
                                                Holidays.end_date >= date)\
            .all()
        if len(res) == 0:
            print('no holidays')
            return False
        else:
            return True

start_date = datetime.datetime.strptime('20-04-2015', '%d-%m-%Y')
France().is_holiday(start_date)
Germany().is_holiday(start_date)
UK().is_holiday(start_date)
print(France().get_zones(start_date))