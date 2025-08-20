# tds_w7_data-story

# Customer Retention Analysis — 2024 (Quarterly)

**Contact / Verification:** 23f3004310@ds.study.iitm.ac.in

## Executive Summary

The company’s average customer retention rate for 2024 is **71.27%** (computed from quarterly values). The industry benchmark target is **85%**. The current retention performance places the company **13.73 percentage points below** the industry benchmark — a material gap with direct implications for revenue and lifetime value.

**Solution recommendation:** implement targeted retention campaigns.

## Data

Quarterly retention rates (2024):
- Q1: 65.53
- Q2: 69.74
- Q3: 76.36
- Q4: 73.44

Average (reported / computed): **71.27**

## Key Findings

1. **Upward recovery mid-year, but inconsistent:** Retention improved from Q1 (65.53) to Q3 (76.36), but slipped back in Q4 (73.44), indicating retention gains are not yet stable.
2. **Volatility suggests cohort-specific issues:** The quarter-to-quarter fluctuations (lowest 65.53 to highest 76.36) indicate that some cohorts or seasonal behaviors are affecting retention.
3. **Material gap vs. benchmark:** 71.27 vs. 85.00 target → a shortfall of 13.73 percentage points. Closing even half of that gap would materially increase customer lifetime value (CLV) and revenues.

## Business Implications

- **Revenue impact:** Lower retention increases churn and the cost of replenishing user base via acquisition — acquisition costs are typically higher than retention costs.
- **Resource allocation:** Strategic investments should prioritize retention (product, customer success, personalized marketing) rather than only ramping acquisition.
- **Operational focus:** The pattern suggests possible product/UX issues or insufficient targeted engagement post-onboarding.

## Recommendations (Actionable)

1. **Segmented retention campaigns (Immediate)**  
   - Identify cohorts with biggest decline (by onboarding month, channel, region, or product) and run targeted re-engagement offers (discounts, personalized content).  
   - A/B test content and incentives, track lift per cohort.

2. **Improve onboarding & early activation (0–30 day) (Short-term)**  
   - Strengthen first 30 days with guided flows, email+SMS sequences, and product tours to increase initial activation and reduce early churn.

3. **Loyalty & incentives (Short-to-Mid term)**  
   - Launch a loyalty program targeted at high-value segments (e.g., customers with >X transactions or spend).  
   - Offer time-limited benefits to customers who are at-risk of churn.

4. **Product improvements driven by feedback (Mid-term)**  
   - Run targeted NPS and exit surveys for cohorts with poor retention, prioritize quick-win product changes.

5. **Measurement & monitoring (Immediate)**  
   - Implement cohort-based retention dashboards (weekly) with alerts for sudden declines.  
   - Evaluate retention by acquisition channel and campaign to optimize marketing spend.

6. **Test budget allocation (Mid-term)**  
   - Run controlled experiments where part of budget shifts from acquisition to retention campaigns to measure ROI.

**Primary solution to implement:** **implement targeted retention campaigns** (cohort-specific, with tailored incentives and A/B testing). Focus initial pilot on cohorts showing highest decline (likely Q1 cohorts or specific acquisition channels).

## Visualization

A trend plot (quarterly retention with industry benchmark) accompanies this analysis. See `artifacts/retention_trend.png` or open `artifacts/report.html`.

## Code & Reproducibility

Included:
- `analysis.py` — generates the plot and `report.html`.
- `requirements.txt` — Python packages needed.
- Scripts were created to be deterministic and reproducible. The code asserts computed average equals **71.27** to ensure data integrity.

## Next Steps (Suggested roadmap)

1. Run cohort analysis (by signup month, channel, region).
2. Pilot 2–3 targeted retention campaigns for top-at-risk cohorts.
3. Build retention dashboard and automated alerts.
4. Reallocate a test budget and measure impact on retention & CAC.

---

**Prepared by:** Senior Data Analytics Team  
**Contact:** 23f3004310@ds.study.iitm.ac.in
