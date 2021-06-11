# Black Scholes Option Pricing
  
[![Followers](https://img.shields.io/github/followers/AlbertLin0327?style=social)](https://github.com/AlbertLin0327)
[![Stars](https://img.shields.io/github/stars/AlbertLin0327?style=social)](https://github.com/AlbertLin0327)
![Issue](https://img.shields.io/github/issues/AlbertLin0327/Black-Scholes-Option-Pricing)
![Commit](https://img.shields.io/github/last-commit/AlbertLin0327/Black-Scholes-Option-Pricing)
  
## Program Description   
This program is to calculate price and greak letter for regular option by Black Scholes method. Since using Black Scholes, price and greak letter can be compute efficiently within O(1). There are also different pricing models and I will work on them in the near future.  
  
The formula for Black Scholes pricing and and greak letters is shown below. If you wish to dig into more, there are abundant of resource on the internet and I am planing on writing a medium on it.
  
- Call Price ![Call Price]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/CallPrice.png?raw=true')
- Put Price ![Put Price]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/PutPrice.png?raw=true')
- Delta ![Delta]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/delta.png?raw=true')
- Gamma ![Gamma]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/gamma.png?raw=true')
- Vega ![Vega]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/vega.png?raw=true')
- Rho ![Rho]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/rho.png?raw=true')
- Theta ![[Theta]('https://github.com/AlbertLin0327/Black-Scholes-Option-Pricing/blob/main/images/theta.png?raw=true')
    
## Basic Information  
Author: Albert Lin    
School: National Taiwna University    
Version: Python3   
Library: Numpy Scipy Decimal   
    
## Usage
### Input format   
- Inputs: *S (stock price), X (strike price), r (continuously compounded annual interest rate in percentage), d (continuously compounded annual dividend rate in percentage), s (annual volatility in percentage), T (time to maturity in years), t (current time in year).*   
- Ex: 
```
100 110 5 1 30 2 0.5  
```  
  
### Output format   
- Output: Call/ Put Option price and greak letter  
- Ex:  
```
 Call Option 
Call Option Price: 12.91346
Call Delta: 0.52694
Call Gamma: 0.01066
Call Vega: 47.94845
Call Rho: 59.67123
Call Theta: -6.56279

 Put Option 
Put Option Price: 16.45405
Put Delta: -0.45817
Put Gamma: 0.01066
Put Vega: 47.94845
Put Rho: -93.40644
Put Theta: -1.64954
```
  
## Reference   
[Quantative Finance Fintech  Prof.Han](http://mx.nthu.edu.tw/~chhan/mainframe.html)  


## Links to Me!
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@linhsinkai)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/hsinkai.lin.327)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/albert-hk-lin)
