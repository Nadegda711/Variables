# Hello!
kvdz = '12'#количество выполненных домашних заданий
kzh = "1.5"#количество затраченных часов
nc = "Python"#название курса
has = "60"#минут в часе
time_for_1_task = ''
print(kzh)
print(kvdz)
print(nc)
print(has)
print(type(kvdz))
print(float(kzh)*60)#количество затраченных минут
print((float(kzh)*60)/float(kvdz))#среднее время выполнения в минутах
print(((float(kzh)*60)/float(kvdz))/float(has))
print(nc, kvdz, kzh, (((float(kzh)*60)/float(kvdz))/float(has)))