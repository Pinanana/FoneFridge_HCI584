import pandas as pd
import datetime


def date_mech(self):
    today = datetime.datetime.today().date()
    ex = datetime.timedelta(days=int(res["expiration (days)"]))
    notif = datetime.timedelta(days=int(res["notify (days)"]))
    expiration = today + ex
    notification = expiration - notif
    #when adding a new row use today, expiration, and notification in the dict.
