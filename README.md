# StockFinancialRatios
Generate Sharpe, Sortino, Information, Treynor, Calmar, and Omega ratios for financial risk analysis from Alpaca historical market price data.

## Purpose

Computing these financial ratios for stocks serves several purposes:

* Performance Evaluation: These ratios help investors and analysts evaluate the historical performance of a stock or a portfolio. They can provide insights into how well a stock has performed compared to a benchmark or the market in general.

* Risk Assessment: Ratios such as the Sharpe Ratio, Sortino Ratio, Information Ratio, and Treynor Ratio help investors understand the risk-adjusted performance of a stock or a portfolio. By considering both returns and risk, investors can make more informed decisions about their investments.

* Portfolio Optimization: Financial ratios can be used to optimize a portfolio by selecting stocks with the desired risk-return characteristics. For example, investors might choose stocks with high Sharpe Ratios to maximize returns per unit of risk.

* Investment Strategy: By analyzing these ratios, investors can develop and refine their investment strategies. For example, they might focus on stocks with high Omega Ratios to capture more upside potential than downside risk, or use Calmar Ratios to identify investments with favorable risk-return profiles in the context of drawdowns.

* Comparison: Investors can use these financial ratios to compare different stocks or portfolios and identify the best opportunities based on their investment goals and risk tolerance.

These financial ratios help investors analyze stock performance, assess risk, optimize their portfolios, and develop effective investment strategies.

## Installation

Install the required packages with pip.

```
pip install -r requirements.txt
```

Make the python and bash scripts executable and create a data directory with read/write permissions.

```
chmod 711 *.py *.sh
mkdir ./data
chmod +rw ./data
```

The python scripts read Alpaca keys from environment variables on you system.

```
export APCA_API_KEY_ID="your-key-here"
export APCA_API_SECRET_KEY="your-secret-key-here"
export APCA_API_BASE_URL="https://paper-api.alpaca.markets"
```

## Example Script Execution

```
./financial_ratios.sh -l momentum.lis -n 504 -f sip -r SPY -c 9

Usage: ./financial_ratios.sh [-n num_days] [-l stock_list] [-f feed_source] [-r reference_stock] [-c sort_column]
```

The output should look something like this:

```
Symbol  Days Cumulative Return   Sharpe Ratio  Sortino Ratio Information Ratio  Treynor Ratio   Calmar Ratio    Omega Ratio Weighted Average
UVXY     504          -92.9153    -1.02448759    -0.09428734       -0.04563430     0.24216486    -0.05595367     0.88476785      -0.19945279
TQQQ     504          -25.5560     0.29023981     0.01954656        0.01292831    -0.07454607    -0.03061733     1.03454096       0.17775724
CPRT     504           42.3718     1.43556306     0.09385706        0.06394506     0.35544243     0.35256986     1.19165259       0.68134557
ARES     504           58.9073     1.47615920     0.09590084        0.06575336     0.37607662     0.39840544     1.19056028       0.70271516
CTAS     504           37.2435     1.45210676     0.09534408        0.06468198     0.36879515     0.53621873     1.19279542       0.70782949
EXTR     504           93.0274     1.43736675     0.08824217        0.06402540     0.62888313     0.41963052     1.19985966       0.74298664
AJG      504           42.2603     1.47278536     0.08729271        0.06560307     0.48790917     0.81841356     1.19171548       0.76444920
CLH      504           61.6604     1.44621384     0.08388651        0.06441948     0.64245388     0.65596292     1.19345735       0.77051621
AAPL     504           46.4708     1.71205030     0.11819431        0.07626078     0.34841283     0.46123172     1.23621442       0.78430721
PANW     504           85.5434     1.43271848     0.11265042        0.06381835     0.73333289     0.64382609     1.21864082       0.79164073
JBL      504           62.9061     1.67593548     0.10968480        0.07465210     0.50460904     0.66512778     1.22144725       0.82176212
ANET     504           89.0194     1.60545868     0.10745428        0.07151281     0.63755635     0.60073265     1.25474170       0.82333845
NVDA     504          131.7443     1.72293144     0.14707467        0.07674547     0.59610769     0.26475367     1.23714662       0.82338048
SD       504          139.6721     1.44734972     0.10987267        0.06447008     1.15715290     0.46788499     1.18525885       0.85937142
MLI      504           70.9544     1.52197860     0.12006692        0.06779432     0.65531509     1.28568216     1.21029692       0.86804732
YPF      504          122.9126     1.43863979     0.12428521        0.06408211     1.19448805     0.51057126     1.17530842       0.87034277
GRBK     504          123.1239     1.64749277     0.13144653        0.07338516     0.82761302     0.60044005     1.23699834       0.87714209
ADMA     504          134.1040     1.42537891     0.11156850        0.06349142     1.14760270     0.76019741     1.18869419       0.88068621
SNPS     504           79.3447     1.79502197     0.13673425        0.07995663     0.57374627     0.77093624     1.26420376       0.89211236
ON       504          130.0742     1.78738393     0.14078964        0.07961641     0.66531514     1.00405780     1.23758602       0.92956216
AVGO     504           74.6988     1.97182768     0.15806636        0.08783219     0.56871010     0.55592585     1.28507976       0.92978738
VAL      504          126.0538     1.54574224     0.11257379        0.06885283     1.21811828     0.83183664     1.19187345       0.93911738
CDNS     504           85.3397     1.93997299     0.13540825        0.08641326     0.62356605     0.86014600     1.27683209       0.95612589
ORLY     504           69.4757     1.59119635     0.08184295        0.07087752     1.18162559     1.00891935     1.22765295       0.96079759
PWR      504           92.6814     1.82983695     0.13790009        0.08150742     0.85672110     1.39998151     1.26768991       1.02279321
HDSN     504          198.0583     1.64221938     0.11981301        0.07315027     1.49007747     1.16440890     1.24828602       1.06322843
ACGL     504           79.5846     1.78428569     0.11552570        0.07947840     1.14663806     1.70948429     1.24040777       1.09065551
ASRT     504          254.7486     1.64893615     0.12989484        0.07344945     1.90719917     0.70350955     1.22977728       1.10277328
HLIT     504          152.1186     1.79658851     0.13659119        0.08002641     1.43528347     1.26070874     1.29921914       1.11734691
FSLR     504          174.3001     1.78768302     0.13564700        0.07962973     1.80716370     0.67443473     1.27377059       1.12765055
NVO      504           97.2139     1.72616558     0.10125219        0.07688953     1.81206191     1.45210781     1.23818169       1.17723039
BLDR     504          181.5858     2.38586247     0.16398984        0.10627476     1.19747782     0.95029849     1.33510518       1.22722012
BORR     504          286.0825     1.69348760     0.13327648        0.07543393     2.54203823     0.58126395     1.23929506       1.23270851
TNK      504          149.7687     1.50504432     0.11822062        0.06704000     2.62877667     1.08243813     1.18958668       1.23481923
CTIC     504          286.5385     1.52297003     0.14042674        0.06783848     2.85071759     0.79949639     1.30307248       1.27216061
LNTH     504          261.0342     2.07088144     0.16480644        0.09224439     2.13342515     1.10680480     1.36297895       1.33711356
CEIX     504          242.0488     1.79315410     0.12303579        0.07987343     2.66377833     1.14696165     1.23584702       1.34157726
ASC      504          185.9091     1.66397565     0.13011933        0.07411937     2.92067905     1.12053453     1.20804700       1.34962246
VKTX     504          322.7704     1.61274022     0.18510312        0.07183716     3.49977496     0.45201855     1.32022953       1.40520621
AMPH     504          150.2680     1.70436005     0.09721624        0.07591823     3.25852594     1.05773328     1.26860592       1.42268219
LLY      504          118.2190     2.03831295     0.15388769        0.09079368     2.22671591     2.06912179     1.27969070       1.43157522
MCK      504          101.2586     2.09044310     0.13615285        0.09311574     2.29889277     2.25608988     1.28921813       1.47798443
BLU      504          319.1977     1.55502186     0.20004029        0.06926618     3.57180528     1.22137357     1.34555763       1.48449541
TDW      504          233.8235     1.88972280     0.13987096        0.08417494     3.35388586     1.54212216     1.24704584       1.55300250
ISEE     504          455.9211     1.89689457     0.19971586        0.08449440     3.46289777     1.26616729     1.37947803       1.57460507
RMBS     504          231.9127     2.91926849     0.21522860        0.13003455     1.92710568     1.30067883     1.46791013       1.59410976
WFRD     504          346.1922     2.23439893     0.16741248        0.09952804     3.42795661     0.90153698     1.30305426       1.61980542
ELF      504          284.8884     2.79093964     0.22754696        0.12431833     2.59389855     1.66505723     1.46842354       1.72735090
SMCI     504          509.5853     2.58772329     0.23233558        0.11526636     3.69590643     3.23042615     1.46204403       2.04273904
VIST     504          434.5679     2.52176156     0.23024332        0.11232819     4.72586123     2.18918390     1.33823380       2.11172397
TH       504          306.8966     1.78267762     0.15528323        0.07940677     7.02826941     1.41518984     1.26881632       2.24785511
AEHR     504         1460.7547     2.41273551     0.23738593        0.10747178     6.73436098     1.09038517     1.41843922       2.37979965
```

The output is sorted by the last column, but you can change this using a command-line parameter.  The Weighted averages are computed using these weights:

```
1. Sharpe Ratio: 0.3 (higher importance for risk-adjusted returns)
2. Sortino Ratio: 0.2 (emphasis on downside risk)
3. Information Ratio: 0.1 (lesser importance for active management)
4. Treynor Ratio: 0.2 (equal importance to Sortino for systematic risk-adjusted returns)
5. Calmar Ratio: 0.1 (lesser importance for maximum drawdown risk)
6. Omega Ratio: 0.1 (lesser importance for higher moments of return distribution)

weighted_average = (sharpe_ratio * 0.3) + (sortino_ratio * 0.2) + (information_ratio * 0.1) + (treynor_ratio * 0.2) + (calmar_ratio * 0.1) + (omega_ratio * 0.1)
```

## What do the columns and various financial ratios mean?

* Sharpe Ratio: A measure of risk-adjusted returns that evaluates the excess return of an investment compared to a risk-free asset per unit of volatility. Higher ratios indicate better risk-adjusted performance.
* Sortino Ratio: A measure of risk-adjusted returns that focuses on the downside risk by measuring the excess return over a target return (usually zero) per unit of downside deviation. It penalizes only the downside volatility of an investment. Higher ratios indicate better risk-adjusted performance in managing downside risk.
* Information Ratio: A measure of risk-adjusted returns that evaluates the excess return of an investment compared to its benchmark per unit of tracking error. It measures the manager's ability to generate alpha or excess returns compared to the benchmark. Higher ratios indicate better performance relative to the benchmark.
* Treynor Ratio: A measure of risk-adjusted returns that evaluates the excess return of an investment compared to the risk-free rate per unit of systematic risk (beta). It measures how much excess return is generated for each unit of systematic risk taken on. Higher ratios indicate better performance relative to the amount of systematic risk taken on.
* Calmar Ratio: A measure of risk-adjusted returns that evaluates the ratio of annualized return to maximum drawdown. It measures how much return is generated per unit of downside risk. Higher ratios indicate better performance in generating returns while minimizing downside risk.
* Omega Ratio: A measure of risk-adjusted returns that evaluates the ratio of the probability-weighted average return of an investment to its probability-weighted average loss for returns below a certain threshold. It measures the amount of expected return per unit of expected loss. Higher ratios indicate better performance in generating positive returns while minimizing negative returns.

## Extra Credit

The Python scripts can be compiled using Cython.  If you would like the scripts to execute faster, you could install the following packages:

```
sudo apt update
sudo apt install python3 black cython3 gcc
```

Execute the following script, to compile the python code.

```
./compile_all.sh
```

This will generate compiled C code, which you could use to modify the `financial_ratios.sh` bash script.  Simply remove the `.py` extensions in the script.

## License

This project is licensed under the MIT License - see the [license](LICENSE) file for details.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Disclaimer

The information provided in this repository is for educational and informational purposes only and should not be construed as financial advice. Trading and investing involve significant risks, and it is essential to do your own research and make informed decisions.

The repository owners, contributors, and anyone associated with this repository do not assume any responsibility or liability for any losses, damages, or other consequences that may arise from the use of the information provided in this repository.

Please consult with a licensed financial advisor or professional before making any financial decisions.
