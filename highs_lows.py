import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # print the index and corresponding header information
    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)

    dates = []
    highs = []
    lows = []
    for row in reader:
        # error check
        try:
            currrent_date = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(currrent_date,'missing data')
        else:
            dates.append(currrent_date)
            highs.append(high)
            lows.append(low)

    # print(highs)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Tempetature (F)",fontsize=16)

plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()