from api_client import get_crypto_prices

def main():
    """
    Main function to fetch and print cryptocurrency prices.
    """
    try:
        prices = get_crypto_prices()
        print("Cryptocurrency Prices (USD):")
        for crypto, price in prices.items():
            print(f"- {crypto}: ${price:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
