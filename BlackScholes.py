# import necessary libraries
import numpy as np
from scipy import stats
from decimal import Decimal


# Class for European Put Option
class BlackScholes:
	def __init__(self, stock, strike, interest, dividend, volatility, maturity, current = 0):
		self.stock_price = Decimal(stock)
		self.strike_price = Decimal(strike)
		self.interest_rate = Decimal(interest / 100)
		self.dividend_rate = Decimal(dividend / 100)
		self.volatility_rate = Decimal(volatility / 100)
		self.time = Decimal(maturity)
		self.now = Decimal(current)

	# Calculate d1 for black scholes
	def calculate_d1d2(self):

		# Calculate d1 and d2
		self.d1 = (Decimal(np.log(float(self.stock_price / self.strike_price))) + \
				  (self.interest_rate - self.dividend_rate + (self.volatility_rate ** 2) / 2) * (self.time - self.now)) / \
		          (self.volatility_rate * np.sqrt(self.time - self.now))

		self.d2 = self.d1 - self.volatility_rate * np.sqrt(self.time - self.now)

		self.d1, self.d2 = float(self.d1), float(self.d2)


	# Calculate Call price and put price
	def pricing(self):

		# Calculate d1 and d2
		self.calculate_d1d2()

		# Calculate call price
		self.call_price = self.stock_price * np.exp(-self.dividend_rate * (self.time - self.now)) * Decimal(stats.norm.cdf(self.d1, 0.0, 1.0)) - \
						  self.strike_price * np.exp(-self.interest_rate * (self.time - self.now)) * Decimal(stats.norm.cdf(self.d2, 0.0, 1.0))

		# Calculate put price
		self.put_price = self.strike_price * np.exp(-self.interest_rate * (self.time - self.now)) * Decimal(stats.norm.cdf(-self.d2, 0.0, 1.0)) - \
						 self.stock_price * np.exp(-self.dividend_rate * (self.time - self.now)) * Decimal(stats.norm.cdf(-self.d1, 0.0, 1.0))

	def calculate_delta(self):

		# Delta: partial Price to partial Stock price
		self.call_delta = np.exp(-self.dividend_rate * (self.time - self.now)) * Decimal(stats.norm.cdf(self.d1, 0.0, 1.0))

		self.put_delta = -np.exp(-self.dividend_rate * (self.time - self.now)) * Decimal(stats.norm.cdf(-self.d1, 0.0, 1.0))


	def calculate_gamma(self):

		# Gamma: second partial Price to second partial Stock price
		self.call_gamma = np.exp(-self.dividend_rate * (self.time - self.now)) * Decimal(stats.norm.pdf(self.d1, 0.0, 1.0)) / \
						  (self.stock_price * self.volatility_rate * np.sqrt((self.time - self.now)))

		self.put_gamma = self.call_gamma

	def calculate_vega(self):

		# Vega: partial Price to partial Volatility rate
		self.call_vega = self.stock_price * np.exp(-self.dividend_rate * (self.time - self.now)) * np.sqrt(self.time - self.now) * Decimal(stats.norm.pdf(self.d1, 0.0, 1.0))

		self.put_vega = self.call_vega

	def calculate_rho(self):

		# Rho: partial Price to partial Interest Rate
		self.call_rho = self.strike_price * np.exp(-self.interest_rate * (self.time - self.now)) * (self.time - self.now) * Decimal(stats.norm.cdf(self.d2))

		self.put_rho = -self.strike_price * np.exp(-self.interest_rate * (self.time - self.now)) * (self.time - self.now) * Decimal(stats.norm.cdf(-self.d2))

	def calculate_theta(self):

		# Theta: partial Price to partial Time
		self.call_theta = self.stock_price * np.exp(self.dividend_rate * (self.time - self.now)) * self.dividend_rate * Decimal(stats.norm.cdf(self.d1, 0.0, 1.0)) - \
						  self.strike_price * np.exp(self.interest_rate * (self.time - self.now)) * self.interest_rate * Decimal(stats.norm.cdf(self.d2, 0.0, 1.0)) - \
						  self.stock_price * np.exp(-self.dividend_rate * (self.time - self.now)) * self.volatility_rate / (2 * np.sqrt(self.time - self.now)) * Decimal(stats.norm.pdf(self.d1, 0.0, 1.0))

		self.put_theta = -self.stock_price * np.exp(self.dividend_rate * (self.time - self.now)) * self.dividend_rate * Decimal(stats.norm.cdf(-self.d1, 0.0, 1.0)) + \
						 self.strike_price * np.exp(self.interest_rate * (self.time - self.now)) * self.interest_rate * Decimal(stats.norm.cdf(-self.d2, 0.0, 1.0)) - \
					     self.stock_price * np.exp(-self.dividend_rate * (self.time - self.now)) * self.volatility_rate / (2 * np.sqrt(self.time - self.now)) * Decimal(stats.norm.pdf(self.d1, 0.0,  1.0))
			  
	def greek_letter(self):

		# Calculate Greek Letter for risk Management
		self.calculate_delta()
		self.calculate_gamma()
		self.calculate_vega()
		self.calculate_rho()
		self.calculate_theta()

