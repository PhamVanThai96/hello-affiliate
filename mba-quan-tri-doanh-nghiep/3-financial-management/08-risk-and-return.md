# Risk and Return – Rủi Ro & Lợi Nhuận (CAPM, Beta)

> **Mục tiêu**: Hiểu mối quan hệ risk-return, CAPM, Beta, diversification, Efficient Frontier, Sharpe Ratio – nền tảng cho mọi quyết định đầu tư.

---

## I. ĐỊNH NGHĨA VÀ LÝ THUYẾT NỀN TẢNG

### 1. Định nghĩa

**Risk** (Rủi ro) trong tài chính là **sự không chắc chắn** về return tương lai. Đo lường bằng **variance/standard deviation** của returns.

**Return** (Lợi nhuận) là **phần thưởng** nhà đầu tư nhận được cho việc chịu đựng rủi ro.

> **Nguyên lý cốt lõi**: **Higher Risk → Higher Expected Return**. Không có "free lunch" – muốn return cao phải chấp nhận risk cao.

### 2. Nguồn gốc lý thuyết

| Học giả | Đóng góp | Năm |
|---------|----------|-----|
| **Harry Markowitz** | Modern Portfolio Theory (MPT), Diversification | 1952 |
| **William Sharpe** | CAPM (Capital Asset Pricing Model) | 1964 |
| **John Lintner** | CAPM (independently developed) | 1965 |
| **Eugene Fama** | Efficient Market Hypothesis | 1970 |
| **Fama & French** | 3-Factor Model (market, size, value) | 1993 |
| **Stephen Ross** | APT (Arbitrage Pricing Theory) | 1976 |

### 3. Các loại rủi ro

```
┌──────────────────────────────────────────────────────────────┐
│                    TOTAL RISK                                 │
│              (Standard Deviation σ)                           │
├──────────────────────────┬───────────────────────────────────┤
│                          │                                   │
│  SYSTEMATIC RISK         │  UNSYSTEMATIC RISK                │
│  (Market Risk)           │  (Specific/Idiosyncratic Risk)    │
│  β × Market movement    │  Company-specific events           │
│                          │                                   │
│  • Recessions           │  • CEO scandal                    │
│  • Interest rate ↑↓     │  • Product recall                 │
│  • Inflation            │  • Lawsuit                        │
│  • War/Pandemic         │  • Competition from new entrant   │
│  • Government policy    │  • Earnings miss                  │
│                          │                                   │
│  CANNOT diversify away!  │  CAN be diversified away!         │
│  → Rewarded by market    │  → NOT rewarded (no premium)      │
│                          │                                   │
│  Measured by: BETA (β)   │  Eliminated by: ~20-30 stocks     │
│                          │                                   │
└──────────────────────────┴───────────────────────────────────┘
```

### 4. Biểu đồ Diversification

```
Total Risk (σ)
  │
  │  ●
  │    ●
  │      ●  ← Unsystematic risk (diversifiable)
  │        ●
  │          ●
  │            ●
  │              ●───●───●────●────●────── → approaches market risk
  │─────────────────────────────────────── ← Systematic risk (β)
  │                                            (cannot eliminate)
  │
  └──┬────┬────┬────┬────┬────┬────┬────→ Number of stocks
     1    5   10   15   20   25   30
     
~90% unsystematic risk eliminated with 20-30 stocks
```

---

## II. PHÂN TÍCH ĐỊNH LƯỢNG

### A. Return Measurement

#### Single Period Return

$$R = \frac{P_1 - P_0 + D}{P_0} = \frac{Capital\,Gain + Income}{Price_{initial}}$$

#### Expected Return (Portfolio)

$$E(R_p) = \sum_{i=1}^{n} w_i \times E(R_i)$$

#### Arithmetic vs Geometric Mean Return

| | Arithmetic | Geometric |
|-|-----------|-----------|
| Formula | $(R_1 + R_2 + ... + R_n) / n$ | $[(1+R_1)(1+R_2)...(1+R_n)]^{1/n} - 1$ |
| Use | Expected future return | Historical actual return |
| Always | Higher (or equal) | Lower (or equal) |

**Ví dụ**: Year 1: +50%, Year 2: -50%
- Arithmetic: (50% + (-50%))/2 = **0%** ← Misleading!
- Geometric: [(1.5)(0.5)]^(1/2) - 1 = **-13.4%** ← Real loss!
- $100 → $150 → $75 (LOST 25%!)

---

### B. Risk Measurement

#### Variance and Standard Deviation

$$\sigma^2 = \sum_{i=1}^{n} p_i \times [R_i - E(R)]^2$$

$$\sigma = \sqrt{\sigma^2}$$

#### Coefficient of Variation (CV) – Risk per unit of return

$$CV = \frac{\sigma}{E(R)}$$

| Investment | E(R) | σ | CV | Better risk-adjusted? |
|-----------|------|---|---|---------------------|
| Stock A | 15% | 25% | 1.67 | |
| Stock B | 12% | 15% | 1.25 | ✅ Less risk per return |
| Stock C | 20% | 40% | 2.00 | |

---

### C. Portfolio Theory (Markowitz, 1952)

#### Portfolio Risk (2 assets)

$$\sigma_p^2 = w_A^2\sigma_A^2 + w_B^2\sigma_B^2 + 2w_Aw_B\sigma_A\sigma_B\rho_{AB}$$

- $\rho_{AB}$ = Correlation coefficient (-1 ≤ ρ ≤ +1)
- $\rho = +1$: Perfect positive correlation (no diversification benefit)
- $\rho = 0$: Uncorrelated (good diversification)
- $\rho = -1$: Perfect negative correlation (eliminate ALL risk!)

#### Diversification Magic

**Example**: Stock A: E(R)=12%, σ=20%. Stock B: E(R)=8%, σ=15%. ρ=0.3

50/50 Portfolio:
- $E(R_p) = 0.5(12\%) + 0.5(8\%) = 10\%$
- $\sigma_p = \sqrt{0.25(0.04) + 0.25(0.0225) + 2(0.25)(0.20)(0.15)(0.3)}$
- $\sigma_p = \sqrt{0.01 + 0.005625 + 0.0045} = \sqrt{0.020125} = 14.19\%$

→ Portfolio σ = 14.19% < Weighted average σ (17.5%) → **Diversification reduces risk!**

#### Efficient Frontier

```
E(Return)
  │              ╭── Efficient Frontier
  │            ╱ │
  │          ╱   │
  │        ╱     │ ← Maximum return for given risk
  │      ╱       │
  │    ●╱        │ ← Minimum Variance Portfolio (MVP)
  │   ╱│         │
  │  ╱  │        │
  │ ╱   ● ← Individual stocks (below frontier = inefficient)
  │╱    │
  │     │
  └─────┼────────────────→ Risk (σ)
        │
   Only portfolios ON the frontier are "efficient"
   (maximum return for given risk level)
```

---

### D. Capital Asset Pricing Model (CAPM) – Sharpe (1964)

#### The Formula

$$E(R_i) = R_f + \beta_i \times [E(R_m) - R_f]$$

Trong đó:
- $E(R_i)$ = Expected return of asset i
- $R_f$ = Risk-free rate
- $\beta_i$ = Beta of asset i (systematic risk measure)
- $E(R_m)$ = Expected market return
- $[E(R_m) - R_f]$ = Market Risk Premium (MRP)

#### Beta (β) – Systematic Risk Measure

$$\beta_i = \frac{Cov(R_i, R_m)}{Var(R_m)} = \frac{\rho_{i,m} \times \sigma_i}{\sigma_m}$$

| β Value | Meaning | Example |
|---------|---------|---------|
| β = 0 | Zero systematic risk | Risk-free asset (T-bill) |
| β = 0.5 | Half market volatility | Utilities, Consumer Staples |
| β = 1.0 | Moves with market | S&P 500 index fund |
| β = 1.5 | 1.5x market moves | Tech stocks, Financial stocks |
| β = 2.0 | 2x market moves | Leveraged companies, small-cap growth |
| β < 0 | Moves OPPOSITE market | Gold (sometimes), VIX |

#### Security Market Line (SML)

```
E(Return)
  │                             ╱ SML
  │                           ╱
  │                 ●       ╱ ← Undervalued! (above SML: return > fair for risk)
  │               ╱       ╱
  │             ╱       ╱
  │           ╱   ●  ╱ ← Fairly priced (on SML)
  │ E(Rm)──╱─────╱──────
  │       ╱    ╱
  │     ╱  ● ╱ ← Overvalued! (below SML: return < fair for risk)
  │   ╱   ╱
  │ Rf──╱─────────── (β=0: risk-free rate)
  │   ╱
  └──┼────┼────┼────┼────────→ Beta (β)
     0   0.5  1.0  1.5  2.0
```

#### CAPM Examples

**Given**: Rf = 4%, E(Rm) = 10%, MRP = 6%

| Stock | β | E(R) = Rf + β × MRP | Interpretation |
|-------|---|---------------------|----------------|
| Utility | 0.4 | 4% + 0.4×6% = **6.4%** | Low risk, low return |
| Market Index | 1.0 | 4% + 1.0×6% = **10%** | Market return |
| Tech stock | 1.5 | 4% + 1.5×6% = **13%** | High risk, high return |
| Startup | 2.5 | 4% + 2.5×6% = **19%** | Very high risk/return |

---

### E. Capital Market Line (CML) vs SML

| | CML | SML |
|-|-----|-----|
| X-axis | Total risk (σ) | Systematic risk (β) |
| Y-axis | E(Return) | E(Return) |
| Applies to | Efficient portfolios only | ALL assets and portfolios |
| Slope | Sharpe Ratio of market | Market Risk Premium |
| Formula | $E(R_p) = R_f + \frac{E(R_m)-R_f}{\sigma_m} \times \sigma_p$ | $E(R_i) = R_f + \beta_i \times MRP$ |

---

### F. Performance Measures

#### Sharpe Ratio (Risk-adjusted return using total risk)

$$Sharpe = \frac{R_p - R_f}{\sigma_p}$$

→ Return per unit of TOTAL risk. Higher = better.

#### Treynor Ratio (Risk-adjusted return using systematic risk)

$$Treynor = \frac{R_p - R_f}{\beta_p}$$

→ Return per unit of SYSTEMATIC risk. For well-diversified portfolios.

#### Jensen's Alpha (Excess return vs CAPM prediction)

$$\alpha = R_p - [R_f + \beta_p(R_m - R_f)]$$

→ α > 0: Outperformed risk-adjusted benchmark (manager skill)

#### Comparison

| Measure | Risk used | Best for |
|---------|----------|----------|
| **Sharpe** | Total σ | Comparing undiversified portfolios |
| **Treynor** | Systematic β | Comparing well-diversified portfolios |
| **Jensen's Alpha** | Systematic β | Evaluating manager skill |
| **Information Ratio** | Tracking error | Active manager vs benchmark |

---

## III. ƯU ĐIỂM VÀ NHƯỢC ĐIỂM

### ✅ Ưu điểm CAPM/MPT:
1. **Simple & Intuitive** – Linear relationship, easy to compute
2. **Widely used** – Standard for Ke calculation, performance evaluation
3. **Systematic risk focus** – Only reward non-diversifiable risk (makes economic sense)
4. **Benchmark** – SML provides fair return for given risk level
5. **Portfolio construction** – Efficient Frontier guides optimal allocation
6. **Empirical support** (partial) – Higher β → Higher average returns (long-term)

### ❌ Nhược điểm:
1. **Single factor** – Only market risk matters? Fama-French shows size, value also matter
2. **Beta unstable** – β changes over time, different estimation windows → different β
3. **Ex-ante vs Ex-post** – CAPM is forward-looking but tested with historical data
4. **Assumptions unrealistic** – Perfect market, rational investors, homogeneous expectations
5. **Market portfolio unobservable** – True "market" = ALL assets (stocks, bonds, RE, human capital)
6. **Empirical anomalies** – Low-β stocks often outperform (Betting Against Beta)
7. **MRP estimation** – 5%? 7%? 10%? Huge debate, affects all calculations
8. **Single period** – Static model, doesn't capture dynamic risk

### CAPM Alternatives

| Model | Factors | Improvement |
|-------|---------|-------------|
| **Fama-French 3-Factor** | Market + SMB (size) + HML (value) | Explains size & value premiums |
| **Carhart 4-Factor** | + Momentum (WML) | Explains momentum anomaly |
| **Fama-French 5-Factor** | + RMW (profitability) + CMA (investment) | More comprehensive |
| **APT** | Multiple macro factors | Flexible, fewer assumptions |
| **Black-Litterman** | Equilibrium + investor views | Better portfolio optimization |

---

## IV. CASE STUDY THÀNH CÔNG: Yale Endowment – MPT & Diversification in Action

### Bối cảnh
- Yale University Endowment: Chief Investment Officer David Swensen (1985-2021)
- Strategy: Apply MPT with EXTREME diversification (alternative assets)
- Result: 13.7% annualized return (1985-2021) vs 9.9% for S&P 500

### Yale's Asset Allocation (MPT-driven)

| Asset Class | Yale Allocation | Typical Endowment | Correlation with S&P |
|-------------|----------------|-------------------|---------------------|
| US Equity | 2.3% | 30% | 1.00 |
| Foreign Equity | 11.4% | 20% | 0.85 |
| Private Equity | 41.0% | 10% | 0.60 |
| Real Assets | 9.8% | 5% | 0.30 |
| Absolute Return (Hedge) | 23.5% | 10% | 0.20 |
| Fixed Income | 4.5% | 25% | -0.20 |
| Cash | 7.5% | 5% | 0.00 |

### Why it worked (MPT reasoning):
1. **Low correlations** – PE, Real Assets, Hedge Funds have low ρ with public markets
2. **Efficient Frontier push** – Adding alternatives → Higher return for same σ
3. **Illiquidity premium** – Accept lock-up → Extra 3-5% return
4. **Systematic rebalancing** – Sell winners, buy losers → contrarian alpha

### Performance

| Period | Yale | 60/40 Portfolio | Value Added |
|--------|------|----------------|-------------|
| 20-year average | 11.3% | 7.5% | +3.8%/yr |
| 2008 GFC | -24.6% | -22% | Slightly worse (illiquidity) |
| 2009-2021 | +14.5%/yr | +11%/yr | +3.5%/yr |
| Risk (σ) | 12% | 10% | Slightly higher |
| Sharpe Ratio | 0.75 | 0.55 | Much better |

### Bài học
1. **Diversification WORKS** – Especially with truly uncorrelated assets
2. **Illiquidity premium is real** – Accept lock-up = extra returns
3. **Efficient Frontier is achievable** – But requires expertise & access
4. **Long-term horizon** – Endowments can adopt strategies retail cannot

---

## V. CASE STUDY THẤT BẠI: Long-Term Capital Management (LTCM) – When Models Fail

### Bối cảnh
- 1994-1998: LTCM – hedge fund founded by Nobel laureates (Merton, Scholes!)
- Strategy: Quantitative arbitrage, "risk-free" convergence trades
- Leverage: 25:1 → Final: 100:1+
- Result: Lost $4.6B in months, nearly collapsed global financial system

### The CAPM/Risk Failure

| LTCM Assumption | Reality |
|----------------|---------|
| **Correlations stable** | During crisis, ALL correlations → 1.0 (everything falls together!) |
| **Normal distribution** | Fat tails: "6-sigma events" happened multiple times |
| **Markets rational** | Panic selling, contagion, liquidity spiral |
| **Historical data = future** | 1998 Russian crisis = unprecedented |
| **Diversification works** | In crisis, diversification FAILED (all assets correlated) |
| **Leverage is manageable** | 25:1 → tiny move = massive loss → margin calls → forced selling |

### Timeline of Collapse

| Date | Event | LTCM Equity |
|------|-------|-------------|
| Jan 1998 | Peak | $4.7B |
| May 1998 | Russian crisis begins | $4.0B |
| Aug 1998 | Russia defaults | $2.3B |
| Sep 1998 | Correlations spike to 1.0 | $0.6B |
| Sep 23, 1998 | Fed-orchestrated bailout | $0.4B (saved from $0) |
| Loss | | **-$4.6B in 5 months!** |

### Key Lessons on Risk

```
1. CORRELATION IS NOT CONSTANT:
   In normal times: ρ = 0.3 (diversification works)
   In crisis: ρ → 1.0 (EVERYTHING drops together!)
   → Models using historical ρ FAIL in crisis

2. FAT TAILS KILL:
   Normal distribution says 4σ event = once per 31,000 years
   Reality: happens every 5-10 years in markets!
   → VaR and Gaussian models UNDERESTIMATE tail risk

3. LEVERAGE AMPLIFIES EVERYTHING:
   25:1 leverage: 4% loss → 100% equity gone!
   If "impossible" event happens → Fund destroyed instantly

4. LIQUIDITY RISK ≠ MARKET RISK:
   You can be "right" on value but can't survive margin calls
   → "Market can stay irrational longer than you can stay solvent" – Keynes

5. MODEL RISK:
   Nobel laureates with best models still failed
   → Models are maps, not territory. Reality is messier.

6. SYSTEMIC RISK:
   Individual risk management ≠ system stability
   When everyone follows same model → crowded trades → simultaneous exit
```

---

## VI. LƯU Ý VỀ PHƯƠNG PHÁP

### Beta Estimation Issues

| Issue | Problem | Solution |
|-------|---------|---------|
| **Time period** | 2 vs 5 years → different β | Use 3-5 year weekly data |
| **Market proxy** | S&P 500? MSCI World? VN-Index? | Match to relevant market |
| **Mean reversion** | β tends to revert to 1.0 over time | Adjusted β = 2/3(raw) + 1/3(1.0) |
| **Business change** | Company changes industry → β changes | Use forward-looking/peer β |
| **Leverage effect** | D/E changes → β changes | Unlever/relever (Hamada) |

### Risk Measures Beyond σ and β

| Measure | Definition | Better for |
|---------|-----------|-----------|
| **VaR** (Value at Risk) | Max loss at x% confidence | Regulatory, banking |
| **CVaR** (Conditional VaR) | Expected loss beyond VaR | Tail risk |
| **Max Drawdown** | Largest peak-to-trough loss | Fund evaluation |
| **Downside Deviation** | σ of ONLY negative returns | Sortino Ratio |
| **Skewness** | Asymmetry of returns | Preference for positive skew |
| **Kurtosis** | Fat tails (leptokurtic) | Tail risk assessment |

---

## VII. CHECKLIST RISK & RETURN

```
UNDERSTANDING:
□ Distinguish systematic vs unsystematic risk?
□ Understand diversification benefit?
□ Know relationship: more risk → more expected return?
□ Can interpret β? (what β=1.3 means)
□ Understand Efficient Frontier concept?

CALCULATION:
□ Can calculate portfolio E(R)?
□ Can calculate portfolio σ (2-asset)?
□ Can apply CAPM: E(R) = Rf + β × MRP?
□ Can compute Sharpe Ratio?
□ Can interpret Jensen's Alpha?

APPLICATION:
□ Use CAPM for Cost of Equity (Ke)?
□ Evaluate portfolio performance risk-adjusted?
□ Construct diversified portfolio (low correlations)?
□ Understand when CAPM/MPT assumptions break down?
□ Know alternatives (Fama-French, APT)?

RISK MANAGEMENT:
□ Not over-leveraged?
□ Stress test for extreme scenarios?
□ Understand correlation instability in crisis?
□ Know about tail risks (fat tails)?
□ Maintain liquidity buffer?
```

---

*Tài liệu tham khảo: Markowitz "Portfolio Selection" (1952); Sharpe "Capital Asset Prices" (1964); Fama & French "Common Risk Factors" (1993); Lowenstein "When Genius Failed" (LTCM); CFA Level I – Portfolio Management & Equity Investments*
