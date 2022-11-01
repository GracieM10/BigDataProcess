#!/usr/bin/python3
import sys
import datetime

uber1 = dict()
uber2 = dict()
rd_l = list()
veh_l = list()
trip_l = list()
vt_l = list()
key = list()
rst = list()
rstt = list()

inp_name = sys.argv[1]
out_name = sys.argv[2]

with open(inp_name,'r') as f:
    def get_days(y,m,d):
        days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        return days[datetime.date(y,m,d).weekday()]
    
    for line in f:
        nline = line.rstrip('\n')
        word = nline.split(',')
        reg = word[0]
        
        day = word[1].split('/')
        day_y = int(day[2]); day_m = int(day[0]); day_d = int(day[1])
        weekday = get_days(day_y,day_m,day_d)
        
        rd = reg + ',' + weekday
        rd_l.append(rd)
        
        veh = word[2]
        veh_l.append(veh)
        trip = word[3]
        trip_l.append(trip)
    
    for i, j in zip(rd_l,veh_l):
        if i not in uber1:
            uber1[i] = int(j)
        else:
            uber1[i] += int(j)
    for i, j in zip(rd_l,trip_l):
        if i not in uber2:
            uber2[i] = int(j)
        else:
            uber2[i] += int(j)

    for keys, values in uber1.items():
        rst.append(keys + ' ' +  str(values) + ',')

    for i, values in zip(rst, uber2.values()):
        i += str(values)
        rstt.append(i)
        
    
    with open(out_name,'w') as out:
        for i in rstt:
            out.write(i + '\n')
            
