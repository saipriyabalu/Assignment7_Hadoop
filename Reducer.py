# #!/usr/bin/env python
# import sys
#
# quakes = {}
# totalmag = 0
#
# # Partitoner
# for line in sys.stdin:
#     line = line.strip()
#     qdate = line.split('\t')[0]
#     mag=line.split('\t')[-1]
#     # print float(mag)
#
#
#     if qdate in quakes:
#         quakes[qdate].append(float(mag))
#
#     else:
#         quakes[qdate] = []
#         quakes[qdate].append(float(mag))
#
#
# #Reducer
# totalmag=0
# for dates in sorted(quakes.keys()):
#    totalmag =sum(quakes[dates])
#    print 'Date:%s Total: %s' % (dates, totalmag)
#
# tmag=0
# for m in sorted(quakes.keys()):
#     if sum(quakes[m])< tmag:
#         flag =1
#     else:
#         flag =0
#
# if flag ==1:
#     print "Magnittude is decreasing"
# else:
#     print "Magnitude is not consistent"
#

#Reference: http://rare-chiller-615.appspot.com/mr1.html

import sys

import datetime

quakes = {}
quakes_day={}

# Partitoner
for line in sys.stdin:
    line = line.strip()
    qdate = line.split('\t')[0]
    mag = line.split('\t')[-1]
    year = qdate.split('-')[0]
    month = qdate.split('-')[1]
    date = qdate.split('-')[2]
    week = datetime.date(int(year), int(month), int(date)).isocalendar()[1]
    day_date=datetime.datetime.strptime(qdate,'%Y-%m-%d').strftime('%A')

#Append magnitude to key-date
    if qdate in quakes:
        quakes[qdate].append(float(mag))

    elif qdate not in quakes:
        quakes[qdate] = []
        quakes[qdate].append(float(mag))

# Append magnitude to key-day
    if day_date in quakes_day :
        quakes_day[day_date].append(float(mag))

    elif day_date not in quakes_day:
        quakes_day[day_date] = []
        quakes_day[day_date].append(float(mag))

# Append magnitude to key-week
    if week in quakes:
        quakes[week].append(float(mag))
    else:
        quakes[week] = []
        quakes[week].append(float(mag))

#Reducer
# Increasing date by date
totalmag=0
for dates in sorted(quakes.keys()):
    totalmag =sum(quakes[dates])
    #print dates,totalmag
    print 'Date:%s Total: %s' % (dates,totalmag)

# Check whether the values are increasing-date
tt=0
for s in sorted(quakes.keys()):
    if sum(quakes[s]) < tt:
        flag = 1
    else:
        flag = 0
if flag==1:
    print "The magnitude is inconsistent"
else:
    print "The magnitude is increasing"


# Increasing day by day
for day in sorted(quakes_day.keys()):
    totalmag=sum(quakes_day[day])
    #print day,totalmag
    print 'Day:%s Total: %s' % (day, totalmag)


# Check whether the values are increasing-day
day_pattern=0
for s in sorted(quakes_day.keys()):
    if sum(quakes_day[s]) < day_pattern:
        flag = 1
    else:
        flag = 0
if flag==1:
    print "The magnitude is inconsistent"
else:
    print "The magnitude is increasing"


#Increasing week by week

totalmag = 0
for dates in sorted(quakes.keys()):
    totalmag = sum(quakes[dates])
    print 'Week:%s Total: %s' % (dates, totalmag)

tmag = 0
for m in sorted(quakes.keys()):
    if sum(quakes[m]) < tmag:
        flag = 1
    else:
        flag = 0

if flag==1:
    print "The magnitude is inconsistent"
else:
    print "The magnitude is increasing"





