A1, A2, A3 = input().split(" ")
B1, B2, B3 = input().split(" ")
code1, unit1, value1 = A1, A2, A3
code2, unit2, value2 = B1, B2, B3
(total) = float((int(unit1)*float(value1))+(int(unit2)*float(value2)))
print("VALOR A PAGAR: R$ %0.2f"%total)