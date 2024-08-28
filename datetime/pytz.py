from datetime import datetime
import pytz

#Lista de Timezones
#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

data = datetime.now(pytz.timezone("Europe/Oslo"))

print(data)