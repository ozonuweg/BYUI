highPrice = 0
year_high = ""

lowPrice = 99999999999999999999999999999999999999
year_low = ""

file_name = input("What is the name of the file? ")

with open(file_name) as stock_price_file:
    next(stock_price_file)

    for line in stock_price_file:
        parts = line.split(",")

        year = parts[0]
        stockPrice = float(parts[1])

        # Find Highest Stock price by time in the Dataset
        if stockPrice > highPrice:
            highPrice = stockPrice
            year_high = year
        
        # Find Lowest Stock price by time in the Dataset
        if stockPrice < lowPrice:
            lowPrice = stockPrice
            year_low = year
    
    buy_shares = lowPrice * 100
    sell_shares = highPrice * 100

    print(f"\nIn {year_low}, we found the lowest stock price. It was ${lowPrice}")
    print(f"In {year_high}, we found the highest stock price. It was ${highPrice}\n")
    print(f"The best time to buy is at the lowest. Time travel to {year_low} to buy shares.")
    print(f"The best time to sell is at the highest. Time travel to {year_high} to sell shares.\n")
    print(f"Marty McFly bought 100 shares for ${buy_shares:.2f} and made ${sell_shares:.2f} when he sold 100 shares.\n")