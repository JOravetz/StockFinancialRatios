# StockFinancialRatios
Generate Sharpe, Sortino, Information, Treynor, Calmar, and Omega ratios for financial risk analysis.

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
chmod 770 ./data
```

The python scripts read Alpaca keys from environment variables on you system.

```
export APCA_API_KEY_ID="your-key-here"
export APCA_API_SECRET_KEY="your-secret-key-here"
export APCA_API_BASE_URL="https://paper-api.alpaca.markets"
```

## Example Script Execution

```
./financial_ratios.sh -l momentum.lis
```

The output should look something like this:

```
Symbol  Days Cumulative Return   Sharpe Ratio  Sortino Ratio Information Ratio  Treynor Ratio   Calmar Ratio    Omega Ratio Weighted Average
UVXY     504          -92.5270    -0.91614678    -0.08184563       -0.04080842     0.00040280    -0.04399977     0.89582251      -0.21003117
SPY      504           -0.4289     0.00000000     0.00000000        0.00000000    -0.00006799    -0.00631903     0.00000000      -0.00064550
TQQQ     504          -47.6686    -0.10112476    -0.00743560       -0.00450445    -0.00004068    -0.06172880     0.98824135       0.06036812
ASO      504           98.0526     1.50767362     0.12917983        0.06715712     0.00057361     0.49915100     1.20295068       0.65517865
MMC      504           33.7583     1.49897152     0.10622090        0.06676950     0.00027467     0.65759217     1.20379847       0.66380658
ERX      504          151.6238     1.59884383     0.12062667        0.07121816     0.00083704     0.65394780     1.20374018       0.69683651
AQUA     504           74.1078     1.62758606     0.13604279        0.07249845     0.00044209     0.54606257     1.23965862       0.70139476
BORR     504          251.5000     1.63672195     0.14312007        0.07290539     0.00175883     0.52700803     1.23031512       0.70301522
DVN      504          127.7160     1.60241530     0.12452729        0.07137725     0.00089040     0.69766891     1.20970030       0.70368277
CDNS     504           59.8619     1.64903253     0.12776431        0.07345375     0.00036376     0.62920731     1.22268670       0.71287015
COP      504          100.4889     1.60432838     0.12227255        0.07146247     0.00096520     0.82591081     1.20846252       0.71652964
BLDR     504           92.8293     1.70623745     0.13011572        0.07600186     0.00048612     0.54466966     1.22499170       0.72255793
FSLR     504          136.3126     1.69843026     0.13858342        0.07565410     0.00101078     0.55217460     1.24177109       0.72440790
STNG     504          183.2966     1.69510160     0.13325813        0.07550583     0.00224771     0.63738097     1.21170085       0.72809041
CNQ      504           98.3213     1.66855168     0.12657983        0.07432320     0.00081457     0.76175599     1.21313567       0.73096587
VTNR     504          472.7941     1.66991164     0.19957205        0.07438378     0.00195665     0.47811104     1.34829819       0.73135853
AJG      504           45.2363     1.69312825     0.12086914        0.07541793     0.00038611     0.87111526     1.22352110       0.74919495
ARCH     504          169.5114     1.63436411     0.13316440        0.07280036     0.00180353     1.04543290     1.21980318       0.75110646
ORLY     504           68.1378     1.66607678     0.10976377        0.07421296     0.00082073     0.99170842     1.24238932       0.75277100
RRC      504          165.8859     1.66233180     0.13817692        0.07404614     0.00107713     1.02037835     1.21842010       0.75783481
OXY      504          141.2066     1.63188289     0.14342767        0.07268984     0.00112966     1.10767955     1.22059252       0.75857252
PWR      504           75.0931     1.65267240     0.14025962        0.07361588     0.00054270     1.16597792     1.23870781       0.77179234
GWW      504           60.5296     1.62332195     0.13687319        0.07230851     0.00054033     1.29310123     1.23104352       0.77412461
FIX      504           79.1039     1.74695952     0.14865924        0.07781576     0.00054266     0.92736268     1.25089577       0.77953566
LNG      504           97.3684     1.61550177     0.12870688        0.07196017     0.00110426     1.44667191     1.20847601       0.78332357
YPF      504          190.2116     1.82652623     0.16061262        0.08135994     0.00126443     0.72859764     1.22712865       0.78404190
WWE      504           96.8245     1.73420661     0.16118607        0.07724770     0.00114922     1.07992024     1.25235941       0.79368178
MSI      504           56.4365     1.89459043     0.15038437        0.08439177     0.00043278     0.65227714     1.27269538       0.79947699
SD       504          242.1182     1.88192093     0.15904512        0.08382742     0.00136652     0.72525152     1.24696356       0.80226286
ANET     504          103.2745     1.95032405     0.17749003        0.08687434     0.00056673     0.68230682     1.30368685       0.82799537
ERF      504          176.1639     1.81896531     0.14198662        0.08102315     0.00114402     1.22431084     1.23433870       0.82828299
RXDX     504          690.4355     1.67108670     0.26791064        0.07443612     0.00305126     1.46898873     1.46364181       0.85622505
XOM      504          100.3319     1.79096162     0.13621061        0.07977577     0.00110330     1.61003477     1.23440603       0.85717292
SMCI     504          183.9276     1.82457744     0.16834721        0.08127314     0.00091041     1.50641516     1.28894084       0.86888767
TRGP     504          117.3537     1.97847957     0.15751247        0.08812848     0.00080131     1.09622819     1.26271961       0.86991426
MPC      504          120.0539     1.98271873     0.15292292        0.08831731     0.00103197     1.11648667     1.25310649       0.87139764
HSY      504           68.1984     1.68520443     0.12587561        0.07506497     0.00138814     2.19014184     1.21829661       0.87936442
ISEE     504          443.5714     1.89817739     0.22640419        0.08455154     0.00174606     1.24160858     1.37223250       0.88492253
HDSN     504          283.0097     1.90902372     0.16739330        0.08503467     0.00131616     1.53408223     1.29440253       0.89780095
ACLS     504          196.3882     2.11844316     0.16586263        0.09436296     0.00066549     1.00058911     1.29484332       0.90781811
LNTH     504          251.7722     2.07150778     0.20087477        0.09227229     0.00115211     1.07663999     1.36181580       0.91493052
ASC      504          269.3878     2.00053932     0.16763566        0.08911110     0.00259135     1.52848991     1.25299908       0.92126721
BTU      504          538.6486     2.07215504     0.17440202        0.09230112     0.00277476     1.32140482     1.29674940       0.92812740
MCK      504           88.7449     1.95664918     0.14999621        0.08715608     0.00133428     2.01460439     1.26722993       0.95415989
TDW      504          265.2529     2.04892402     0.16758349        0.09126633     0.00224414     1.69888272     1.27047971       0.95470561
AEHR     504         1048.2301     2.23930422     0.24227641        0.09974654     0.00175990     0.88267133     1.38135575       0.95697589
RMBS     504          138.6723     2.37331323     0.19636258        0.10571577     0.00075999     0.86237792     1.35545892       0.98377374
ACGL     504           91.1106     2.08491266     0.16128643        0.09286939     0.00089894     1.92228586     1.28639599       0.98806600
NVO      504          126.3962     2.13663731     0.15446338        0.09517339     0.00154699     1.81239169     1.30330426       0.99328020
CPRX     504          269.8690     2.13958556     0.16612472        0.09530472     0.00146391     1.97297424     1.34300668       1.01652196
LLY      504          122.0332     2.18303550     0.17943530        0.09724013     0.00144931     2.12485266     1.30079638       1.04337649
ELF      504          206.5124     2.56748816     0.22982001        0.11436501     0.00107507     1.29961167     1.40034353       1.09785749
CEIX     504          584.7380     2.54044509     0.20563733        0.11316042     0.00249448     2.18298498     1.35188598       1.16856303
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

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

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
