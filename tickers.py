#!/usr/bin/env python3

import os
import argparse
import pandas as pd

# Import Alpaca API's REST client
from alpaca_trade_api.rest import REST


class TickerList:
    """Fetches a list of all active assets from the Alpaca API and stores it in a user-defined file"""

    def __init__(self, api_key, secret_key, base_url):
        """Initializes the Alpaca REST API client with provided API keys and base URL"""
        self.rest_api = REST(api_key, secret_key, base_url)

    def fetch_and_save(self, file_name):
        """Fetches the list of active assets, saves it to a text file with the provided file name"""
        # Fetch the list of active assets from Alpaca API
        assets = self.rest_api.list_assets(status="active")

        # Extract symbols and names from the assets
        symbols = [el.symbol for el in assets]
        names = [el.name for el in assets]

        # Create a DataFrame with symbols as index and names as a column
        df = pd.DataFrame(index=symbols, columns=["names"])
        df["names"] = names

        # Save the DataFrame to a text file
        with open(file_name + ".txt", "w") as tfile:
            tfile.write(df.to_csv(sep="|", header=None))

        print(
            f"Successfully saved the list of active assets to {file_name}.txt"
        )


if __name__ == "__main__":
    # Load API keys and base URL from environment variables
    API_KEY_ID = os.environ["APCA_API_KEY_ID"]
    SECRET_KEY_ID = os.environ["APCA_API_SECRET_KEY"]
    BASE_URL = os.environ["APCA_API_BASE_URL"]

    # Define command-line arguments and parse them
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        default="tickers",
        help="The name of the output file (without extension) to store the fetched list output (default: 'tickers')",
    )

    args = parser.parse_args()

    # Create a TickerList object and fetch the list of active assets
    ticker_list = TickerList(API_KEY_ID, SECRET_KEY_ID, BASE_URL)
    ticker_list.fetch_and_save(args.file)
