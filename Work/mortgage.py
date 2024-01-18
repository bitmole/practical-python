# mortgage.py
#
# Exercise 1.7

def calc(start, end, extra_payment):
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    npayments = 0
    total_paid = 0.0

    while principal > 0:
        npayments = npayments + 1
        cur_payment = payment + extra_payment if start <= npayments <= end else payment
        remaining = principal * (1+rate/12)
        if cur_payment > remaining: # overpayment?
            cur_payment = remaining
        principal = remaining - cur_payment 
        total_paid = total_paid + cur_payment
        print(npayments, round(cur_payment, 2), round(total_paid, 2), round(principal, 2))

    print('Total paid', round(total_paid, 2), "in", npayments, "months")

if __name__ == "__main__":
    start = input('start month: ')
    end = input('end month: ')
    extra_payment = input('extra payment: ')
    args = [int(s) for s in (start, end, extra_payment)]
    calc(*args)
