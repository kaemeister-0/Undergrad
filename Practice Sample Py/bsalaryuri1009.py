a=input('')
base_salary=float(input())
sale_money=float(input())
if sale_money > 0:
    total_money=base_salary+(sale_money*0.15)
    print ('TOTAL = R$ %0.2f'%total_money)
elif    sale_money <= 0 :
    print ('TOTAL = R$ %0.2f'%base_salary)