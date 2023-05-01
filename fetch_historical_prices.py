#!/usr/bin/env python3

"""
Script to fetch historical price data for a given list of stock symbols
"""

import os
import argparse
import pandas as pd
import concurrent.futures
import pandas_market_calendars as mcal

from alpaca_trade_api.rest import REST, TimeFrame

# Load API keys and base URL from environment variables
API_KEY_ID = os.environ["APCA_API_KEY_ID"]
SECRET_KEY_ID = os.environ["APCA_API_SECRET_KEY"]
BASE_URL = os.environ["APCA_API_BASE_URL"]

# Initialize REST API client
rest_api = REST(API_KEY_ID, SECRET_KEY_ID, BASE_URL)


def get_historic_prices(universe, date_from, to_end, ndays, max_workers=100):
    """
    Fetch historical prices for stock symbols in the universe.
    """

    def historic_agg_v2(symbol):
        # Get historical data for the given symbol
        data_frame = rest_api.get_bars(
            symbol, TimeFrame.Day, date_from, to_end, adjustment="split"
        ).df
        data_frame.reset_index(inplace=True)
        data_frame["datetime"] = pd.to_datetime(
            data_frame["timestamp"]
        ).dt.strftime("%Y-%m-%d")
        # Filter out rows with 0 values for volume, trade_count, or vwap
        data_frame = data_frame[
            ~(data_frame[["volume", "trade_count", "vwap"]] == 0).any(axis=1)
        ]
        data_frame = data_frame[["datetime", "close"]]
        data_frame.set_index("datetime", inplace=True)

        # Add the latest trade data if it's not in the data_frame
        if data_frame.index[-1] != to_end:
            last_trade = rest_api.get_latest_trade(symbol)
            data_frame.loc[to_end] = [last_trade.price]

        # Get the last ndays of data
        data_frame = data_frame.tail(ndays)

        # Save the data to a file if the number of rows is equal to ndays
        if data_frame.shape[0] == ndays:
            with open(f"./data/{symbol}.dat", "w") as tfile:
                tfile.write(data_frame.to_csv(sep=" ", header=None))

        return

    # Use ThreadPoolExecutor for concurrent fetching of data
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers
    ) as executor:
        results = {}
        future_to_symbol = {
            executor.submit(historic_agg_v2, symbol): symbol
            for symbol in universe
        }
        for future in concurrent.futures.as_completed(future_to_symbol):
            symbol = future_to_symbol[future]
            try:
                results[symbol] = future.result()
            except Exception:
                continue
        return results


def run(args):

    stock_list = str(args.list)
    ndays = int(args.ndays)

    # Read stock symbols from the list file
    with open(stock_list, "r") as f:
        universe = [
            item.upper() for item in f.read().split("\n") if item != ""
        ]
    if "SPY" not in universe:
        universe.append("SPY")

    # Initialize NYSE calendar
    nyse = mcal.get_calendar("NYSE")

    total_days = int(ndays * 1.75)

    # Calculate date range for fetching data
    end_dt = pd.Timestamp.now(tz="America/New_York")
    start_dt = end_dt - pd.Timedelta("%4d days" % total_days)
    date_from = start_dt.strftime("%Y-%m-%d")
    to_end = end_dt.strftime("%Y-%m-%d")

    # Get the NYSE schedule for the given date range
    nyse_schedule = (
        nyse.schedule(start_date=date_from, end_date=to_end)
        .tail(1)
        .index.to_list()
    )

    # Fetch historical prices for the universe of stock symbols
    get_historic_prices(universe, date_from, to_end, ndays)


if __name__ == "__main__":

    # Set up command-line argument parser
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument(
        "--list",
        type=str,
        default="momentum.lis",
        help="List of possible trade Symbols (no default, ex: momentum.lis)",
    )
    PARSER.add_argument(
        "--ndays",
        type=int,
        default="504",
        help="Number of days to fetch historical price data "
        "(default, ex: --ndays 504)",
    )

    # Parse command-line arguments and run the script
    ARGUMENTS = PARSER.parse_args()
    run(ARGUMENTS)
