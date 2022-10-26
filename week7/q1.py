import requests
page = requests.get("http://www.reuters.com/finance/stocks/company-officers/GOOG.O")
page2 = requests.get("http://www.reuters.com/finance/stocks/company-officers/AMZN")
page3 = requests.get("http://www.reuters.com/finance/stocks/company-officers/AAPL") 
print(page.content)
print("\n\n")

print(page2.content)
print("\n\n")
print(page3.content)