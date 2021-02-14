import urllib.request
import json
from string import Template


def getStockData():
    while True:
        inputData = input('Enter a stock symbol. To escape, type "quit".\n')
        if inputData == 'quit': break

        template = Template('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=$stock&apikey=$key')
        apiKey = '2YEW4ZDR6FMS9BFI'
        url = template.substitute(stock=inputData, key=apiKey)
        connection = urllib.request.urlopen(url)
        responseString = connection.read().decode()
        print(responseString)
        stockDict = json.loads(responseString)
        template2 = Template('The current price of $stock is: $price')
        output = template2.substitute(stock=stockDict['Global Quote']['01. symbol'],
                                      price=stockDict['Global Quote']['05. price'])
        print(output)
        print('Stock Quotes retrieved successfully!')
