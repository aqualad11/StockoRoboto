import sys
sys.path.append('../src')
sys.path.append('../webscrapers')
import top_stocks as ts
import alpaca_service as alp
from collections import deque



def sma_200_50_test(symbol):
    # Get data 
    all_data = alp.get_stock_data(symbol, 'day', 1000)

    # Set up vars 
    fifty = deque()
    two = deque()
    fifty_avg = 0
    two_avg = 0

    for x in all_data:
        if(len(two) < 200):
            two.append(x.c)
            two_avg += x.c
            if(len(fifty) < 50):
                fifty_avg += x.c
                fifty.append(x.c)
            else:
                fifty_avg -= fifty.popleft()
                fifty_avg += x.c
                fifty.append(x.c)
            
            if(len(two) == 199):
                two_avg /= 200
                fifty_avg /= 50

        else:
            two.append(x.c)
            fifty.append(x.c)
            
            # Get new Averages
            two_avg += 200
            fifty_avg += 50

            two_avg -= two.popleft()
            fifty_avg -= fifty.popleft()

            two_avg += x.c
            fifty_avg += x.c

            two_avg /= 200
            fifty_avg /= 50
            
            # Check whether to buy or sell
            if(fifty_avg > two_avg):
                buy(symbol, x.c)
            elif(fifty_avg <= two_avg):
                sell(symbol, x.c)

def buy(symbol, price):
    global bought
    if not bought:
        msg = symbol + ' bought at $' + str(price)
        trans.append([msg, price])
        bought = True

def sell(symbol, price):
    global bought
    global total_profit
    if bought:
        profit = price - trans[-1][1]
        msg = symbol + ' sold at $' + str(price) + ' profit = $' + str(profit)
        trans.append([msg, price])
        total_profit += profit
        bought = False

# Globals
bought = False
trans = []
total_profit = 0

sma_200_50_test('NTEC')

for t in trans:
    print(t[0])

print('total profit: ' + str(total_profit))

