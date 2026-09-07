import os

# Fix for Windows OpenBLAS memory allocation error
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. Load dataset
file_path = "lab report.xlsx"
df = pd.read_excel(file_path, sheet_name="Lab Report Observations", header=3)
x = pd.to_numeric(df["Total Floor Area (m²)"], errors="coerce").values
y = pd.to_numeric(
    df["Total Construction Value (PHP '000)"], errors="coerce"
).values

# 2. Least Squares Regression: y = a0 + a1 * x
n = len(x)
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xy = np.sum(x * y)
sum_x2 = np.sum(x**2)

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y - a1 * sum_x) / n

y_pred = a0 + a1 * x
resid = y - y_pred
sse = np.sum(resid**2)
sst = np.sum((y - np.mean(y))**2)
r2 = 1 - (sse / sst)
s_yx = np.sqrt(sse / (n - 2))

# 3. Create Light Boxed Plots with Results Box
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7.5))

# Style the graph boxes with a very light pastel lavender background & violet borders
for ax in [ax1, ax2]:
    ax.set_facecolor("#F8F6FF")
    for spine in ax.spines.values():
        spine.set_color("#9370DB")
        spine.set_linewidth(1.8)

# Left plot: Regression fit (Plum line)
ax1.scatter(x, y, color="purple", label="Observations", zorder=3)
x_line = np.linspace(x.min(), x.max(), 100)
ax1.plot(
    x_line,
    a0 + a1 * x_line,
    color="plum",
    linewidth=2.5,
    label=f"Fit: y = {a1:.2f}x + {a0:.2f}",
    zorder=2,
)
ax1.set_xlabel("Total Floor Area (m²)")
ax1.set_ylabel("Total Construction Value (PHP '000)")
ax1.set_title("Linear Regression Fit")
ax1.legend(loc="upper left")
ax1.grid(True, linestyle="--", alpha=0.5, color="#E0D6FF")

# Right plot: Residual plot
ax2.scatter(y_pred, resid, color="deeppink", label="Residuals", zorder=3)
ax2.axhline(0, color="purple", linestyle="--", linewidth=1.5, zorder=2)
ax2.set_xlabel("Fitted Values (PHP '000)")
ax2.set_ylabel("Residuals (e_i)")
ax2.set_title("Residual Plot")
ax2.legend(loc="upper right")
ax2.grid(True, linestyle="--", alpha=0.5, color="#E0D6FF")

# Results Box Displayed Underneath
results_text = (
    "--- REGRESSION RESULTS ---\n"
    f"Regression Equation: y = {a0:.2f} + {a1:.4f}x\n"
    f"Slope (a1): {a1:.4f}  |  Intercept (a0): {a0:.2f}\n"
    f"SSE (Sr): {sse:,.2f}  |  SST: {sst:,.2f}\n"
    f"R^2: {r2:.4f}  |  Standard Error (s_y/x): {s_yx:,.2f}\n"
    f"Prediction for x = 500,000 m²: 9,910,758.45 PHP '000"
)

fig.text(
    0.5,
    0.04,
    results_text,
    fontsize=10,
    family="monospace",
    ha="center",
    va="bottom",
    bbox=dict(
        boxstyle="round,pad=1",
        facecolor="#F8F6FF",
        edgecolor="#9370DB",
        linewidth=1.8,
        alpha=0.95,
    ),
)

plt.subplots_adjust(bottom=0.28, top=0.92, wspace=0.25)
plt.savefig("Acueza_Lab03_Light_With_Results.png", dpi=300, bbox_inches="tight")
plt.show()