import csv
from datetime import datetime
from matplotlib import pyplot as plt

#Get dates,high and low temperature from file
filename='sitka_weather_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    #print(header_row)
    #for index,column_header in enumerate(header_row):
        #print(index,column_header)
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high=int(row[1])
        highs.append(high)
        low=int(row[3])
        lows.append(low)

    #print(highs)

#plot data
fig=plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Formal plot
plt.title("Daily high and low temperatures - 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',labelsize=16)
plt.show()
