def makeChange(cash, currency):
	'''
	INPUT
	Takes two variables, an integer and a dictionary.
	cash is the amount of money in units of the smallest available unit, e.g. pennies.
	currency has coin names as keys and values as their associated values, e.g. '£2': 200.

	OUTPUT
	Returns another dictionary: keys are coin names and values are numbers of those coins in the cash variable.
		'''
	denom = list(currency.values())
	names = list(currency.keys())
	numcoin = []
	
	for amount in denom:
		if cash >= amount:
			numcoin.append(cash // amount)
			cash = cash % amount
		else:
			numcoin.append("None")
	result = dict(zip(names, numcoin))
	return result

def dictionaryDisplay(myDict):	
	'''
	Displays key/value pairs on separate lines
	'''
	keys = list(myDict.keys())
	values = list(myDict.values())
	dictzip = zip(keys, values)
	for key, value in zip(keys, values):
		print("{}: {}".format(key, value))


'''
Dictionaries of some currency variables:

currency_uk = {'£2': 200, '£1': 100, '50p': 50, '20p': 20, '10p': 10, '5p': 5, '2p': 2, '1p': 1}

currency_us = {'Quarters': 25, 'Dimes': 10, 'Nickels': 5, 'Pennies': 1}

currency_euro = {'€2': 200, '€1': 100, '50c': 50, '20c': 20, '10c': 10, '5c': 5, '2c': 2, '1c': 1}
'''

cash = int(input("Cash in smallest currency unit: "))


currency_uk = {'£2': 200, '£1': 100, '50p': 50, '20p': 20, '10p': 10, '5p': 5, '2p': 2, '1p': 1}

print(makeChange(cash, currency_uk))

#coindisplay = makeChange(cash, currency_uk)

#dictionaryDisplay(coindisplay)
