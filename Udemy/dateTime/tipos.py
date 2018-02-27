'''
Data eh um tipo Linear


Existe 4 tipos de datas
1) date(month, day, year)
2) time(hours, minutes, seconds)
3) datetime(month, day, year, hours, minutes, seconds)
4) timedelta => duracao entre datas
'''

import datetime
d1 = datetime.date(2016,11,24)
d2 = datetime.date(2017,10,24)
print(max(d1,d2), '=> mostra a data maxima')
print(d1-d2, '=> Diferenca entre as datas')
print((d1-d2).days, '=> Diferenca entre as datas em uma saida limpa')


#data de hoje
print(datetime.date.today(), '=> data de hoje')


#datetime
print('=' * 50, 'datetime')
century_start = datetime.datetime(2000,1,1,0,0,0)
time_now = datetime.datetime.now()
print(century_start,time_now)
print("we are",time_now - century_start,"days, hour, minutes and seconds into this century")


#timedelta
print('=' * 50, 'timedelta')
century_start = datetime.datetime(2000,1,1,0,0,0)
time_now = datetime.datetime.now()
time_since_century_start = time_now - century_start
print("days since century start",time_since_century_start.days)
print("seconds since century start",time_since_century_start.total_seconds())
print("minutes since century start",time_since_century_start.total_seconds()/60)
print("hours since century start",time_since_century_start.total_seconds()/60/60)#timedelta

#datetime.time
print('=' * 50, 'datetime.time')
date_and_time_now = datetime.datetime.now()
time_now = date_and_time_now.time()
print(time_now)