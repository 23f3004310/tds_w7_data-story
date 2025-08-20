# analysis.py
"""
Customer retention analysis
Author: Senior Data Analyst (example)
Verification email: 23f3004310@ds.study.iitm.ac.in
"""

import math
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---- Data ----
quarters = ["Q1", "Q2", "Q3", "Q4"]
retention = [65.53, 69.74, 76.36, 73.44]  # given
industry_target = 85.0
reported_average = 71.27  # provided -- we will assert our computed average matches this

# ---- Compute ----
df = pd.DataFrame({"Quarter": quarters, "Retention": retention})
computed_avg = round(df["Retention"].mean(), 2)

# sanity check: ensure the computed average matches the provided reported average 71.27
if computed_avg != reported_average:
    raise AssertionError(f"Computed average {computed_avg} != reported average {reported_average}")

print(f"Computed average retention: {computed_avg}")  # should print 71.27

# ---- Plotting ----
sns.set_style("whitegrid")
sns.set_context("talk")

fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

# line plot of retention
sns.lineplot(data=df, x="Quarter", y="Retention", marker="o", linewidth=3, ax=ax, label="Company Retention")

# industry benchmark line
ax.axhline(industry_target, color="red", linestyle="--", linewidth=2, label=f"Industry Target = {industry_target}")

# annotate points
for i, (q, r) in enumerate(zip(df["Quarter"], df["Retention"])):
    ax.annotate(f"{r:.2f}", (i, r), textcoords="offset points", xytext=(0,8), ha="center", fontsize=12)

# visual styling
ax.set_ylim(55, max(industry_target + 5, df["Retention"].max() + 5))
ax.set_title("Customer Retention Rate — 2024 Quarterly Trend vs. Industry Target", fontsize=16, weight="bold")
ax.set_ylabel("Retention Rate (%)")
ax.set_xlabel("Quarter")
ax.legend()
plt.tight_layout()

# save plot
out_dir = "artifacts"
os.makedirs(out_dir, exist_ok=True)
plot_path = os.path.join(out_dir, "retention_trend.png")
fig.savefig(plot_path)
plt.close(fig)

print(f"Plot saved to: {plot_path}")

# ---- Simple HTML summary (embedded image) ----
html = f"""<!doctype html>
<html>
<head><meta charset="utf-8"><title>Retention Analysis Report</title></head>
<body style="font-family: Arial, sans-serif; margin: 2rem;">
  <h1>Customer Retention Rate — 2024 Quarterly Data</h1>
  <p><strong>Quarters</strong>: {quarters}</p>
  <p><strong>Retention values</strong>: {retention}</p>
  <p><strong>Computed average retention</strong>: {computed_avg}</p>
  <p><strong>Industry benchmark target</strong>: {industry_target}</p>
  <h2>Key visualization</h2>
  <img src="{os.path.basename(plot_path)}" alt="Retention Trend" style="max-width:800px; border:1px solid #ddd;"/>
  <h2>Primary recommendation</h2>
  <p>The recommended primary solution is to <strong>implement targeted retention campaigns</strong> focused on cohorts showing drop-offs. See README.md for details and next steps.</p>
  <hr/>
  <p>Contact: 23f3004310@ds.study.iitm.ac.in</p>
</body>
</html>
"""

html_path = os.path.join(out_dir, "report.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML summary written to: {html_path}")
print("All done.")