import requests
from cachetools import cached, TTLCache

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,dogecoin&vs_currencies=usd"

@cached(cache=TTLCache(maxsize=1024, ttl=60))
def get_crypto_prices():
    """
    Fetches cryptocurrency prices from the CoinGecko API.

    Returns:
        A dictionary containing the prices of Bitcoin, Ethereum, and Dogecoin.

    Raises:
        requests.exceptions.RequestException: If there is an error connecting to the API.
        ValueError: If the API response is not in the expected format.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()

        if not isinstance(data, dict) or not all(k in data for k in ["bitcoin", "ethereum", "dogecoin"]):
            raise ValueError("Unexpected API response format.")

        return {
            "Bitcoin": data["bitcoin"]["usd"],
            "Ethereum": data["ethereum"]["usd"],
            "Dogecoin": data["dogecoin"]["usd"],
        }
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error connecting to CoinGecko API: {e}")
    except KeyError as e:
        raise ValueError(f"Error: Missing key in API response: {e}. Check the API response format.")
