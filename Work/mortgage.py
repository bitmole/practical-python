# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
npayments = 0
total_paid = 0.0

while principal > 0:
    npayments = npayments + 1
    cur_payment = payment + extra_payment if npayments <= 12 else payment
    principal = principal * (1+rate/12) - cur_payment 
    total_paid = total_paid + cur_payment
    print(npayments, round(cur_payment, 2), round(total_paid), round(principal, 2))

print('Total paid', round(total_paid, 2), "in", npayments, "months")
