from datetime import date, time, datetime, timedelta
import dateutil.relativedelta

# Criando objeto date
print(date(year=2021, month=1, day=10))

# Transformar data tipo string para formato date (iso-formated)
print(date.fromisoformat("2022-01-10"))

# Tranformar data tipo date para tipo string
date1 = date(2022, 1, 2)
print(str( date1.isoformat() [:10]))

# Data do dia atual
print(date.today())

# Operacão de adiação e subtração em data
print(date.today() + timedelta(days=1))# +1 dia
print(date.today() + timedelta(days=-1))# -1 dia
print(date.today() + timedelta(days=365))# + ano
print(date.today() + timedelta(days=-365))# - ano

# Extraindo parte em data especifica 
print('Ano inteiro: ',date1.strftime("%Y"))
print('Ano simplificado: ',date1.strftime("%y"))
print('Mês: ',date1.strftime("%m"))
print('Dia: ',date1.strftime("%d"))
