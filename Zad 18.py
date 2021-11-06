wzrost = int(input("Podaj swój wzrost w cm:"))
stopy = int(wzrost * 0.032808)
cale = int(wzrost *0.39370- stopy *12)
print(f'"Masz {wzrost}cm wzrostu to {stopy} stóp i {cale} cali"')
