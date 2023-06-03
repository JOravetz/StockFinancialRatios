#!/usr/bin/env python3

import sys
import math
import argparse
import pandas as pd
import numpy as np

from pathlib import Path
from scipy.stats import skew
from concurrent.futures import ThreadPoolExecutor, as_completed

TRADING_DAYS = 252  # Trading days in a year

# Function to read stock prices from a file and return the last num_days prices as a NumPy array
def read_prices_from_file(file_path, num_days):
    try:
        df = pd.read_csv(
            file_path,
            sep="\s+",
            header=None,
            names=["date", "price"],
            usecols=["date", "price"],
        )
        return df.iloc[0]["date"], df.tail(num_days)["price"].values
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None, None


def calculate_sortino_ratio(returns, target_return=0):
    downside_returns = returns[returns < target_return]
    downside_std = np.std(downside_returns)
    sortino_ratio = (
        np.mean(returns - target_return) / downside_std
        if downside_std > 0
        else np.nan
    )
    return sortino_ratio


def print_ratios(
    symbol,
    days,
    cumulative_return,
    sharpe_ratio,
    sortino_ratio,
    information_ratio,
    treynor_ratio,
    calmar_ratio,
    omega_ratio,
    weighted_average,
    header=False,
):
    print(
        f"{symbol:<6s} {days:>5d} {cumulative_return * 100:>17.4f} {sharpe_ratio:>14.8f} {sortino_ratio:>14.8f} "
        f"{information_ratio:>17.8f} {treynor_ratio:>14.8f} {calmar_ratio:>14.8f} {omega_ratio:>14.8f} {weighted_average:>16.8f}"
    )


def process_stock(args, stock_file):
    symbol = Path(stock_file.name).stem

    reference_symbol = args.reference.upper()  # convert to upper case
    reference_file_path = f"./data/{reference_symbol}.dat"

    # Read reference stock prices and input stock prices
    ref_first_date, ref_prices = read_prices_from_file(
        reference_file_path, args.num_days
    )
    if ref_prices is None:
        return None

    first_date, prices = read_prices_from_file(stock_file, args.num_days)
    if prices is None or first_date != ref_first_date:
        return None

    # Calculate daily returns for both the reference and input stock prices
    daily_returns = np.diff(prices) / prices[:-1]
    ref_daily_returns = np.diff(ref_prices) / ref_prices[:-1]

    # Calculate cumulative returns for both the reference and input stock prices
    cumulative_return = (prices[-1] / prices[0]) - 1
    ref_cumulative_return = (ref_prices[-1] / ref_prices[0]) - 1

    # Calculate market neutral daily returns
    market_neutral_daily_returns = (daily_returns - ref_daily_returns) * 0.5

    # Calculate mean and standard deviation of market neutral daily returns
    mean_daily_returns = np.mean(market_neutral_daily_returns)
    std_daily_returns = np.std(market_neutral_daily_returns)

    # Calculate the Sharpe Ratio
    sharpe_ratio = (
        math.sqrt(len(prices)) * mean_daily_returns / std_daily_returns
        if std_daily_returns > 0
        else 0
    )

    # Calculate the Sortino Ratio
    sortino_ratio = calculate_sortino_ratio(market_neutral_daily_returns)

    # Calculate the Information Ratio
    tracking_error = np.std(market_neutral_daily_returns)
    information_ratio = (
        mean_daily_returns / tracking_error if tracking_error > 0 else 0
    )

    # Calculate the Treynor Ratio
    beta = np.cov(ref_daily_returns, daily_returns)[0, 1] / np.var(
        ref_daily_returns
    )
    excess_return = cumulative_return - ref_cumulative_return  # corrected
    treynor_ratio = excess_return / beta if beta != 0 else 0

    # Calculate the Calmar Ratio
    max_drawdown = np.max(np.maximum.accumulate(prices) / prices - 1)
    annual_return = (prices[-1] / prices[0]) ** (
        TRADING_DAYS / len(prices)
    ) - 1
    calmar_ratio = annual_return / max_drawdown if max_drawdown != 0 else 0

    # Calculate the Omega Ratio
    threshold_return = 0
    gains = np.sum(
        market_neutral_daily_returns[
            market_neutral_daily_returns > threshold_return
        ]
    )
    losses = np.sum(
        market_neutral_daily_returns[
            market_neutral_daily_returns <= threshold_return
        ]
    )
    omega_ratio = gains / -losses if losses != 0 else 0

    # Calculate the Weighted Average
    weighted_average = (
        (sharpe_ratio * 0.3)
        + (sortino_ratio * 0.2)
        + (information_ratio * 0.1)
        + (treynor_ratio * 0.2)
        + (calmar_ratio * 0.1)
        + (omega_ratio * 0.1)
    )

    # Return the financial ratios and the weighted average as a list
    return [
        symbol,
        args.num_days,
        cumulative_return,
        sharpe_ratio,
        sortino_ratio,
        information_ratio,
        treynor_ratio,
        calmar_ratio,
        omega_ratio,
        weighted_average,
    ]


def print_header():
    print(
        f"{'Symbol':>6s} {'Days':>5s} {'Cumulative Return':>17s} {'Sharpe Ratio':>14s} {'Sortino Ratio':>14s} {'Information Ratio':>17s} "
        f"{'Treynor Ratio':>14s} {'Calmar Ratio':>14s} {'Omega Ratio':>14s} {'Weighted Average':>16s}"
    )


def main(args):
    header_printed = False
    if args.symbol:
        args.symbol = args.symbol.upper()

    reference_symbol = Path(args.reference).stem

    if args.list:
        with args.list.open() as f:
            stock_symbols = [line.strip() for line in f]

        data = []

        with ThreadPoolExecutor() as executor:
            futures = []
            for symbol in stock_symbols:
                if symbol == reference_symbol:
                    continue
                try:
                    stock_file = open(f"./data/{symbol}.dat", "r")
                    futures.append(
                        executor.submit(process_stock, args, stock_file)
                    )
                except FileNotFoundError:
                    pass

            for future in as_completed(futures):
                processed_data = future.result()
                if processed_data is not None:
                    data.append(processed_data)

        # If there's no valid data to output, exit the program
        if data is None or not data:
            sys.exit()

        # Sort data by the specified column in ascending order
        data.sort(key=lambda x: x[args.sort_column], reverse=False)

        for row in data:
            print_ratios(*row)
    elif args.symbol:
        stock_file_path = f"./data/{args.symbol}.dat"
        with open(stock_file_path, "r") as stock_file:
            if not header_printed:
                print_header()
                header_printed = True

            processed_data = process_stock(args, stock_file)
            print_ratios(*processed_data, header=True)
    elif not sys.stdin.isatty():
        if not header_printed:
            print_header()
            header_printed = True
        process_stock(args, sys.stdin)
    else:
        parser.print_help()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate financial ratios of stock prices using reference prices."
    )
    parser.add_argument(
        "-r",
        "--reference",
        type=str,
        default="SPY",
        help="Symbol of the reference stock",
    )
    parser.add_argument(
        "-n",
        "--num_days",
        type=int,
        default=504,
        help="Number of days to use in the computations",
    )
    parser.add_argument(
        "-l",
        "--list",
        type=Path,
        help="File containing a list of stock symbols, one per line",
    )
    parser.add_argument(
        "-s", "--symbol", type=str, help="Stock symbol to process"
    )
    parser.add_argument(
        "-c",
        "--sort_column",
        type=int,
        default=9,
        help="Index of the column to sort by (0-based)",
    )
    args = parser.parse_args()
    main(args)
