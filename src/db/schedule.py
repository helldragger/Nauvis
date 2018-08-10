import sqlite3


def read_upcoming_events(db):
    return db.execute("SELECT date, name FROM schedule "
                      "JOIN event USING event_id "
                      "WHERE date >= Datetime('now', 'start of day')"
                      "AND date <= Datetime('now', 'start of day', '+1 month')"
                      "AND state == 0"
                      "ORDER BY Datetime(date) asc")

def read_month(db):
    return db.execute("SELECT * FROM schedule "
                      "WHERE date >= Datetime('now', 'start of day')"
                      "AND date <= Datetime('now', 'start of day', '+1 month')"
                      "ORDER BY Datetime(date) asc")

def read_week():
    return db.execute('SELECT * FROM schedule '
                      'WHERE date > Datetime(?) '
                      'ORDER BY Datetime(date) asc')

def read_day():
    return db.execute('SELECT * FROM schedule '
                      'WHERE date > Datetime(?) '
                      'ORDER BY Datetime(date) asc', )

def read_next(db):
    return db.execute('SELECT * FROM schedule '
                      'WHERE date > Datetime(?) '
                      'LIMIT 1'
                      'ORDER BY Datetime(date) asc')