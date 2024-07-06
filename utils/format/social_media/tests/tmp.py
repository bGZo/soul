from datetime import datetime
print(str(datetime.strptime('2023-06-09T08:30:55.000Z', '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y%m%d, %H:%M:%S')))