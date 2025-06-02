from datetime import datetime
from datetime import date
from datetime import timedelta

print(datetime.today())
print(date.today())

mydatetime = datetime.fromtimestamp(1706551390)
print(mydatetime, type(mydatetime))

ordinal_day = 365 # Порядковий номер дня
dt = datetime.fromordinal(ordinal_day)
print(dt)
day_number = datetime.today().toordinal()
print(f'Порядковий номер сьогоднішнього дня: {day_number}')
current_datetime = datetime.now()
print("Поточна дата і час:", current_datetime)
incoming_date = "Aug 24, 1991"
dt_incoming_date = datetime.strptime(incoming_date, '%b %d, %Y')
print(dt_incoming_date)
dt_incoming_time_out = dt_incoming_date.strftime("%H:%M:%S and %Y-%m-%d")
print(dt_incoming_time_out)

dt_01 = "19:45:23"  # Germany
dt_02 = "20:00:22"
dt_03 = "20:00:27"
dt_04 = "20:45:23"  # Kyiv

def to_hour(time_in_hour:str):
    return datetime.strptime(time_in_hour, "%H:%M:%S")

def array_to_hour(*args):
    for dt in args:
        yield to_hour(dt)

dt_01_dt, dt_02_dt, dt_03_dt = array_to_hour(dt_01, dt_02, dt_03)
print(dt_01_dt, dt_02_dt, dt_03_dt)
diff_time = dt_02_dt - dt_01_dt
print("Diff", diff_time, type(diff_time))

if dt_02_dt - dt_01_dt <= timedelta(minutes=15):
    print("yes")
else:
    print("no")

if dt_03_dt - dt_02_dt <= timedelta(seconds=3):
    print("yes")
else:
    print("no")

d = datetime.today()
print(d)
print(d.isocalendar())
print(d.isoformat())
print(d.isoweekday())
print(d.timetuple())
print(d.weekday())
dd = d.replace(year=2023, day=12)
print(dd)

td = timedelta(days=5, hours=3, minutes=30)
print(td)
total_seconds = td.total_seconds()
print(total_seconds)
