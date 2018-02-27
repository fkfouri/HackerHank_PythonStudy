'''
Conversor de string para data

Biblioteca de formatos datetime.strptime => Convert String em DATA
http://pubs.opengroup.org/onlinepubs/009695399/functions/strptime.html


datetime.strftime => Convert Data em STRING
'''
import datetime

print('=' * 50, 'datetime.strptime => String To Date')
date='01-Apr-03'
date_object=datetime.datetime.strptime(date,'%d-%b-%y')
print(date_object)
print(datetime.datetime.strptime('01/10/2017','%d/%m/%Y'))
print(datetime.datetime.strptime('14/04/1979 22:34:11','%d/%m/%Y %H:%M:%S'))
print(datetime.datetime.strptime('14/04/1979 11:34:11','%d/%m/%Y %I:%M:%S'))



#Unfortunately, there is no similar thing for time delta
#So we have to be creative!
bus_travel_time='2:15:30'
hours,minutes,seconds=bus_travel_time.split(':')
x=datetime.timedelta(hours=int(hours),minutes=int(minutes),seconds=int(seconds))
print(x)



print('=' * 50, 'datetime.strftime => Date to String')
now = datetime.datetime.now()
string_now = datetime.datetime.strftime(now,'%m/%d/%Y %H:%M:%S')
print(now, string_now)
print(str(now)) #Or you can use the default conversion

print(datetime.datetime.strftime(now,'%b.%d.%Y %I:%M:%S'))


