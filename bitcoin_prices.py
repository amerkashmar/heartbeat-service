import requests
import datetime
from datetime import timedelta

def fetch_bitcoin_prices(start_date, end_date):
    """
    Fetch daily Bitcoin open prices from CoinGecko API
    
    Args:
        start_date (datetime): Start date
        end_date (datetime): End date
        
    Returns:
        list: List of dictionaries containing date and open price
    """
    # Convert dates to UNIX timestamps (milliseconds)
    start_timestamp = int(start_date.timestamp() * 1000)
    end_timestamp = int(end_date.timestamp() * 1000)
    
    # CoinGecko API endpoint for Bitcoin market chart
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range"
    
    params = {
        "vs_currency": "usd",
        "from": start_timestamp // 1000,  # Convert to seconds
        "to": end_timestamp // 1000,      # Convert to seconds
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        
        # Extract prices (timestamp, price)
        prices_data = data.get("prices", [])
        
        # Process the data to get daily open prices
        daily_prices = []
        current_date = None
        
        for timestamp_ms, price in prices_data:
            # Convert timestamp to datetime
            timestamp_s = timestamp_ms / 1000
            date = datetime.datetime.fromtimestamp(timestamp_s).date()
            
            # If we have a new date, add it to our results
            if date != current_date:
                current_date = date
                daily_prices.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "open_price": price
                })
        
        return daily_prices
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def main():
    # Define date range
    start_date = datetime.datetime(2025, 2, 6)
    end_date = datetime.datetime(2025, 2, 27)
    
    print(f"Fetching Bitcoin open prices from {start_date.date()} to {end_date.date()}...")
    
    # Fetch Bitcoin prices
    bitcoin_prices = fetch_bitcoin_prices(start_date, end_date)
    
    if bitcoin_prices:
        print("\nBitcoin Daily Open Prices (USD):")
        print("-" * 40)
        
        # Display prices in a list
        for entry in bitcoin_prices:
            print(f"{entry['date']}: ${entry['open_price']:,.2f}")
        
        # Alternative approach using CoinAPI if CoinGecko fails
        print("\nNote: If the CoinGecko API fails due to rate limits or other issues,")
        print("you can try alternative APIs like CoinAPI (requires free API key) or Alpha Vantage.")
    else:
        print("Failed to fetch Bitcoin prices. Please try again later.")
        print("Note: Some cryptocurrency APIs have rate limits for free tier usage.")
        print("You may need to register for a free API key or try a different API.")

if __name__ == "__main__":
    main()
