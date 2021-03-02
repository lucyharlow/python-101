# This version uses floor division instead of rounding down the division of 'cash' by the denomination, reducing two steps to one.

user = int(input("Cash in pennies: "))
cash = user
GBP2 = cash // 200
cash = cash % 200
GBP1 = cash // 100
cash = cash % 100
GBP50 = cash // 50
cash = cash % 50
GBP20 = cash // 20
cash = cash % 20
GBP10 = cash // 10
cash = cash % 10
GBP05 = cash // 5
cash = cash % 5
GBP02 = cash // 2
cash = cash % 2
GBP01 = cash // 1
cash = cash % 1

print(GBP2, GBP1, GBP50, GBP20, GBP10, GBP05, GBP02, GBP01)


