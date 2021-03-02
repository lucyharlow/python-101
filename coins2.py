# This improves on coins1.py by requesting a user input and printing the results together at the bottom. Without knowing floor divison, I simply divided the value for 'cash' by the denomination value and used 'int' for the purpose of rounding down.

cash = int(input("Cash in pennies: "))
GBP2 = int(cash/200)
cash = cash % 200
GBP1 = int(cash/100)
cash = cash % 100
GBP50 = int(cash/50)
cash = cash % 50
GBP20 = int(cash/20)
cash = cash % 20
GBP10 = int(cash/10)
cash = cash % 10
GBP05 = int(cash/5)
cash = cash % 5
GBP02 = int(cash/2)
cash = cash % 2
GBP01 = int(cash/1)
cash = cash % 1
print(GBP2, GBP1, GBP50, GBP20, GBP10, GBP05, GBP02, GBP01)

