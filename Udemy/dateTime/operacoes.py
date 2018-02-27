'''
Operacoes Aritimeticas
'''
import datetime

today=datetime.date.today()
five_days_later= today + datetime.timedelta(days=5)
print(five_days_later, '=> Imprime hoje + 5 dias')
print(today + datetime.timedelta(weeks=-1), '=> hoje menos 1 semana')
print(today + datetime.timedelta(weeks=-1, days = 2), '=> hoje menos 1 semana + 2 dias')



#timedelta
print('=' * 50, 'timedelta')
now = datetime.datetime.today()
five_minutes_and_five_seconds_later = now + datetime.timedelta(minutes=5,seconds=5)
print(five_minutes_and_five_seconds_later, '=> agora + 5 minutos + 5 segundos')