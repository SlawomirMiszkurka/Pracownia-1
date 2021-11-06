a = int(input("Podaj długość pierwszego boku:"))
b = int(input("Podaj długość drugiego boku:"))
c = int(input("Podaj długość trzeciego boku:"))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**(1/2)
print(f"Area: {area}")