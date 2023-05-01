#!/bin/bash

num_days=504
stock_list=""

while getopts "n:l:" opt; do
  case $opt in
    n)
      num_days="$OPTARG"
      ;;
    l)
      stock_list="$OPTARG"
      ;;
    *)
      echo "Usage: $0 [-n num_days] [-l stock_list_file]" >&2
      exit 1
      ;;
  esac
done

rm -f ./data/*.dat

if [ -z "$stock_list" ]; then
  ./tickers.py > /dev/null
  awk -F"|" 'NR>1 && length($1)<5 {print $1}' tickers.txt | sort | uniq > combined.lis 
  stock_list="combined.lis"
fi

./fetch_historical_prices.py --list "$stock_list" --ndays "$num_days"

wc -l ./data/*.dat | awk -v days=504 '{
  if ($1 == days) {
    gsub("./data/", "", $2)
    gsub(".dat", "", $2)
    print $2
  }
}' > good.lis

./financial_ratios_calculator.py -l good.lis > output.txt
cat output.txt

