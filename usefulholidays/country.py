__author__ = 'baptiste'
from usefulholidays.scholarholidays import *
from sqlalchemy import or_
import datetime
session = db.session()

class France:

    def __init__(self):
        self.name = 'France'

    def is_day_off(self, date):
        res = db.session.query(Holidays).filter(Countries.name == self.name,
                                                Countries.id == Holidays.country_id,
                                                Holidays.start_date == date.strftime('%Y-%m-%d %H:%M:%S.%f'),
                                                or_(Holidays.name == 'day-off',
                                                Holidays.name == 'day-off-wdaysensitive'))\
            .all()
        if len(res) == 0:
            return False
        else:
            return True

    def is_holiday(self, date):
        res = db.session.query(Holidays).filter(Countries.name == self.name,
                                                Countries.id == Holidays.country_id,
                                                Holidays.start_date <= date,
                                                Holidays.end_date >= date)\
            .all()
        if len(res) == 0:
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

    def get_zone_and_name(self, date):
        """

        :param date: a datetime.date()
        :return: returns a list of zone and the corresponding holiday name within a list.
        """
        q = db.session.query(Holidays.zone, Holidays.name).filter(Countries.name == self.name,
                                                                  Countries.id == Holidays.country_id,
                                                                  Holidays.start_date <= date,
                                                                  Holidays.end_date >= date,
                                                                  Holidays.zone != self.name)\
            .all()
        res = []
        for zone, hol in q:
            if hol == 'winter' or hol == 'spring':
                res.append(zone.replace(' ','_') + '_' + hol)
            else:
                res.append(hol)
                return res
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
            return False
        else:
            return True


class Belgium:

    def __init__(self):
        self.name = 'Belgium'

    def is_holiday(self, date):
        res = db.session.query(Holidays).filter(Countries.name == self.name,
                                                Countries.id == Holidays.country_id,
                                                Holidays.start_date <= date,
                                                Holidays.end_date >= date)\
            .all()
        if len(res) == 0:
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
            return False
        else:
            return True


def get_all_countries():
    countries = db.session.query(Countries.name).all()
    return countries


def get_countries_in_holidays(date):
    countries = db.session.query(Countries.name).distinct(Countries.name).filter(Holidays.start_date <= date,
                                                        Holidays.end_date >= date,
                                                        Countries.id == Holidays.country_id)\
            .all()
    return countries