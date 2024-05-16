import datetime

UTC_DELTA = 3

def get_time_with_default_utc(time: datetime.time) -> datetime.time:
    dt = datetime.datetime.combine(datetime.date.today(), time)
    new_time = (dt - datetime.timedelta(hours=UTC_DELTA)).time()
    return new_time