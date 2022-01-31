n_s = int(input ('Введите время в секундах:'))
print (n_s)
if n_s < 60:
    print (f"00:00:{n_s:02}")
elif n_s < 3600:
    print (f"00:{n_s // 60:02}:{n_s % 60:02}")
else:
    print (f"{n_s // 3600:02}:{(n_s % 3600) // 60:02}:{n_s % 60:02}")
    