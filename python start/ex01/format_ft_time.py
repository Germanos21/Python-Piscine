from datetime import datetime

dt = datetime.today()
seconds = dt.timestamp()
print(f'Seconds since January 1, 1970: {seconds:,} or {seconds:e} in scientific notation')
print(datetime.today().strftime('%b %d %Y'))