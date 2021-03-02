# The final version, in which I learned how to use for loops properly and how to store the results in the variable 'numcoin'. Commented out below are my initial and unpythonic attempts to display the results: like the loop in coins4.py they work, but not elegantly. Once I learned the zip function, I had a much simpler and better way of displaying the results.

cash = int(input("Cash in pennies: "))
denom = [200, 100, 50, 20, 10, 5, 2, 1]
coins = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
numcoin = []

for value in denom:
	if cash >= value:
		numcoin.append(cash // value)
		cash = cash % value
	else:
		numcoin.append("None")

for coin, num in zip(coins, numcoin):
	print("{}: {}".format(coin, num))

#for i in range(len(coins)):
#	print("{}: {}".format(coins[i], numcoin[i]))

#for i in range(len(coins)):
#	print("Coin {}: {}".format(i, coins[i]))

#for x, y in enumerate(coins, numcoin):
#	print("Coin {}: {}".format(x, y))

#print()
#print("Coin" + "\t" + "Number")
#print()
#	print(coins[i] + "\t" + str(numcoin[i]))
#print()
