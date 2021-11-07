waga = float(input("Podaj swoją wagę w kg:"))
wzrost = float(input("Podaj swój wzrost w cm:"))
bmi = waga / (wzrost/100)**2
print(f"Twoje BMI wynosi {bmi}")
