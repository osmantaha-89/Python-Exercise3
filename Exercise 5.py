income = int(input("what is your income? "))

if income <= 67000:
 tax = (income * 0.24)
elif income <= 97000:
 tax = (income * 0.31)
elif income >= 97000:
 tax = (income * 0.34)

print(f"Your income after taxes is {income - tax} euros")