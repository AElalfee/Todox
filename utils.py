from datetime import datetime


def now_iso():
    return datetime.now().isoformat()


def date_format(iso_date):
    date_format = "%d %b %Y at %H:%M:%S"
    date_object = datetime.fromisoformat(iso_date)
    return date_object.strftime(date_format)