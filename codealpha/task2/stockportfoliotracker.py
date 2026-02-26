def run_stock_tracker():
    stock_prices = {
        "AAPL": 180.0, 
        "TSLA": 250.0, 
        "GOOGL": 140.0, 
        "MSFT": 340.0, 
        "AMZN": 135.0
    }
    
    portfolio = {}
    
    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks to track:", ", ".join(stock_prices.keys()))
    print("Type 'done' when you are finished adding stocks.")
    print("-------------------------------------------------")

    while True:
        ticker = input("\nEnter stock ticker (or 'done' to finish): ").upper()
        
        if ticker == 'DONE':
            break
            
        if ticker not in stock_prices:
            print(f"'{ticker}' is not in our database. Available stocks: {', '.join(stock_prices.keys())}")
            continue
            
        try:
            quantity = float(input(f"Enter quantity of {ticker} shares: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for the quantity.")
            continue
            
        # Add to portfolio (handles multiple entries of the same stock)
        portfolio[ticker] = portfolio.get(ticker, 0) + quantity

    # Calculate Total Investment
    total_investment = 0.0
    summary_output = "\n--- Portfolio Summary ---\n"
    
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_investment += value
        summary_output += f"{stock}: {qty} shares @ ${price:.2f} = ${value:.2f}\n"
        
    summary_output += f"-------------------------\n"
    summary_output += f"Total Investment Value: ${total_investment:.2f}\n"

    print(summary_output)

    # Optional File Handling
    save_file = input("Would you like to save this summary to a .txt file? (y/n): ").lower()
    if save_file == 'y':
        with open("portfolio_summary.txt", "w") as file:
            file.write(summary_output)
        print("Portfolio successfully saved to 'portfolio_summary.txt'.")

# Run the tracker
run_stock_tracker()