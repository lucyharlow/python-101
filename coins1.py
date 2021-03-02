# My first change-making program. I didn't know floor division so I used the modulo operator to subtract the remainder from the 'cash' variable and divide it by the next denomination. I also didn't know how to solicit user input, and changed the variable each time to test different values. It took me a long time to correct a typo a few lines in; this made me realise that having so many lines was inefficient AND was very susceptible to mistakes!

cash = 573
print(cash)
GBP2 = (cash - (cash % 200)) / 200
print(GBP2)
cash = cash % 200
print(cash)
GBP1 = (cash - (cash % 100)) / 100
print(GBP1)
cash = cash % 100
print(cash)
GBP50 = (cash - (cash % 50)) / 50
print(GBP50)
cash = cash % 50
print(cash)
GBP20 = (cash - (cash % 20)) / 20
print(GBP20)
cash = cash % 20
print(cash)
GBP10 = (cash - (cash % 10)) / 10
print(GBP10)
cash = cash % 20
print(cash)
GBP05 = (cash - (cash % 5)) / 5
print(GBP05)
cash = cash % 5
print(cash)
GBP02 = (cash - (cash % 2)) / 2
print(GBP02)
cash = cash % 2
print(cash)
GBP01 = (cash - (cash % 1)) / 1
print(GBP01)
cash = cash % 1
print(cash)
