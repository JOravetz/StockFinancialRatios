#!/bin/bash

num_days=504
feed_source="sip"
stock_list=""
reference_stock="SPY"
sort_column=9  # default sort column

while getopts "n:l:f:r:c:" opt; do
  case $opt in
    n)
      num_days="$OPTARG"
      ;;
    l)
      stock_list="$OPTARG"
      ;;
    f)
      feed_source="$OPTARG"
      ;;
    r)
      reference_stock=$(echo "$OPTARG" | tr '[:lower:]' '[:upper:]')
      ;;
    c)
      sort_column="$OPTARG"
      ;;
    *)
      echo "Usage: $0 [-n num_days] [-l stock_list] [-f feed_source] [-r reference_stock] [-c sort_column]" >&2
      exit 1
      ;;
  esac
done

rm -f ./data/*.dat

if [ -z "$stock_list" ]; then
  python3 tickers.py > /dev/null
  awk -F"|" 'NR>1 && length($1)<5 {print $1}' tickers.txt | sort | uniq > combined.lis 
  stock_list="combined.lis"
else
  awk '{print $1}' "${stock_list}" > tmp.lis ; mv tmp.lis "${stock_list}"
fi

python3 fetch_historical_prices.py --list "$stock_list" --ndays "$num_days" --feed "$feed_source"

wc -l ./data/*.dat | awk -v days="${num_days}" '{
  if ($1 == days) {
    gsub("./data/", "", $2)
    gsub(".dat", "", $2)
    print $2
  }
}' > good.lis

python3 financial_ratios_calculator.py -l good.lis -n "${num_days}" -r "${reference_stock}" -c "${sort_column}" > output.txt
cat output.txt
