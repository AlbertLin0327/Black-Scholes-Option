=== ***Basic Information*** ===  
Author: Albert Lin    
School: National Taiwna University    
Version: Python3   
Library: Numpy Scipy Decimal   
   
=== ***Program Description*** ===   
This program is to calculate price and greak letter for regular option by Black Scholes method. Since using Black Scholes, price and greak letter can be compute efficiently within O(1). However, to keep the formula readable, I choose not to optimize a lot.  
  
=== ***Input format*** ===  
Inputs: S (stock price), X (strike price), r (continuously compounded annual interest rate in percentage), d (continuously compounded annual dividend rate in percentage), s (annual volatility in percentage), T (time to maturity in years), t (current time in year).   
Ex: 100 110 5 1 30 2 0.5  
  
=== ***Output format*** ===  
Output: Call/ Put Option price and greak letter  
Ex:  
```
=== Call Option ===
Call Option Price: 12.91346
Call Delta: 0.52694
Call Gamma: 0.01066
Call Vega: 47.94845
Call Rho: 59.67123
Call Theta: -6.56279

=== Put Option ===
Put Option Price: 16.45405
Put Delta: -0.45817
Put Gamma: 0.01066
Put Vega: 47.94845
Put Rho: -93.40644
Put Theta: -1.64954
```
  
=== ***Reference*** ===  
Quantative Finance Fintech  Prof.Han  
https://quantpie.co.uk/bsm_formula/bs_summary.php  
