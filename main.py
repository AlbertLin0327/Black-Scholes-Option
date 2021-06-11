# Import Black Scholes Model
from BlackScholes import BlackScholes

# Print result
def printInfo(ordinary_option, r):

	print('')

	# print Call option
	print('=== Call Option ===')
	print('Call Option Price:', round(ordinary_option.call_price, r))
	print('Call Delta:', round(ordinary_option.call_delta, r))
	print('Call Gamma:', round(ordinary_option.call_gamma, r))
	print('Call Vega:', round(ordinary_option.call_vega, r))
	print('Call Rho:', round(ordinary_option.call_rho, r))
	print('Call Theta:', round(ordinary_option.call_theta, r))

	print('')

	# print Put option
	print('=== Put Option ===')
	print('Put Option Price:', round(ordinary_option.put_price, r))
	print('Put Delta:', round(ordinary_option.put_delta, r))
	print('Put Gamma:', round(ordinary_option.put_gamma, r))
	print('Put Vega:', round(ordinary_option.put_vega, r))
	print('Put Rho:', round(ordinary_option.put_rho, r))
	print('Put Theta:', round(ordinary_option.put_theta, r))

	print('')



# main function
def main():

	# take in the input from user
	print('Enter: spot price, strike price, interest(%), dividend(%), volatility(%), maturity year, current year')

	while True:
		try:
			stock, strike, interest, dividend, volatility, maturity, current = map(float, input().split())
			break

		except:
			print("WRONG FORMAT!!!")

	# Calculate Information for Black Scholes option
	ordinary_option = BlackScholes(stock, strike, interest, dividend, volatility, maturity, current)
	ordinary_option.pricing()
	ordinary_option.greek_letter()

	# Round to 5 digits by default
	printInfo(ordinary_option, 5)

if __name__ == '__main__':
	main()