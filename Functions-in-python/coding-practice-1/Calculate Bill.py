def calculate_bill(amount):
    if amount < 500:
        bill = amount - (amount * 0.05)
    elif (amount>= 500) and (amount < 2500):
        bill = amount - (amount * 0.1)
    else:
        bill = amount - (amount * 0.2)
    bill = round(bill,3)
    return bill


amount = int(input())
result = calculate_bill(amount)
print(result)