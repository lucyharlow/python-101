# Finally, I learned how to use loops in Python! However, I didn't understand them yet. Although this version works, the counter is redundant, and the variable 'coin' in the first line of the loop is never used. I was thinking in terms of while loops. Furthermore, I set up the formatting of the results within the loop, which made it difficult to make edits, not to mention easy to introduce errors while making those edits.

cash = int(input("Cash in pennies: "))
denom = [200, 100, 50, 20, 10, 5, 2, 1]
result = ['£2', '£1', '50p', '20p', '10p', '5p', '2p', '1p']
count = 0


for coin in denom:
	if cash >= denom[count]:
		result[count] = (result[count] + " coins: " + str(cash // denom[count]))
		cash = cash % denom[count]
		count += 1
	else:
		result[count] = (result[count] + " coins: None")
		count += 1

print(result)
