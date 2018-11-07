import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # print the index and corresponding header information
    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)

    dates = []
    highs = []
    for row in reader:
        currrent_date = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(currrent_date)

        high = int(row[1])
        highs.append(high)

    # print(highs)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate(rotation = 45)
plt.ylabel("Tempetature (F)",fontsize=16)

plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()