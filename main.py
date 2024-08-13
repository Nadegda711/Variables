# Hello!
k_v_d_z = '12'#количество выполненных домашних заданий
k_z_h = "1.5"#количество затраченных часов
n_c = "Python"#название курса
h_a_s = "60"#минут в часе
time_for_1_task = '0.125'
print(k_z_h)
print(k_v_d_z)
print(n_c)
print(h_a_s)
print(type(k_v_d_z))
print(float(k_z_h)*60)#количество затраченных минут
print((float(k_z_h)*60)/float(k_v_d_z))#среднее время выполнения в минутах
print(((float(k_z_h)*60)/float(k_v_d_z))/float(h_a_s))
print(n_c, 'всего задач: ',k_v_d_z, 'затрачено часов: ',k_z_h, 'среднее время выполнения ',(((float(k_z_h)*60)/float(k_v_d_z))/float(h_a_s)), 'часа.' )