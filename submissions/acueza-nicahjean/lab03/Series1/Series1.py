import math
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PALETTE DEFINITIONS (Light Purple, Pink, Blue)
# ==========================================
PURPLE_LIGHT = "#B39DDB"
PURPLE_DARK = "#7E57C2"
PINK_LIGHT = "#F48FB1"
PINK_DARK = "#EC407A"
BLUE_LIGHT = "#64B5F6"
BLUE_DARK = "#1E88E5"

# ==========================================
# EXERCISE 1: Convergence of (1 + 1/n)^n to e
# ==========================================
print("Generating Exercise 1...")

labels_e1 = [
    "yearly",
    "twice a year",
    "quarterly",
    "monthly",
    "weekly",
    "daily",
    "hourly",
    "every minute",
    "every second",
    "every millisecond",
    "every microsecond",
    "every nanosecond",
]

n_values_e1 = [
    1,
    2,
    4,
    12,
    52,
    365,
    365 * 24,
    365 * 24 * 60,
    365 * 24 * 3600,
    365 * 24 * 3600 * 1000,
    365 * 24 * 3600 * 1000000,
    365 * 24 * 3600 * 1000000000,
]

e_exact = math.e
values_e1 = [(1 + 1 / np.float64(n)) ** np.float64(n) for n in n_values_e1]
errors_e1 = [abs(e_exact - val) for val in values_e1]

fig1, (ax1_1, ax1_2) = plt.subplots(1, 2, figsize=(14, 6))
fig1.suptitle(
    "Exercise 1: Convergence of (1 + 1/n)^n to e", fontsize=14, fontweight="bold"
)

# Subplot 1: Values (Soft Blue)
bars1 = ax1_1.bar(
    range(len(labels_e1)),
    values_e1,
    color=BLUE_LIGHT,
    edgecolor=BLUE_DARK,
    width=0.7,
)
ax1_1.axhline(
    y=e_exact,
    color=PINK_DARK,
    linestyle="--",
    label=f"e = {e_exact:.6f}",
    linewidth=1.5,
)
ax1_1.set_title("Value per compounding period", fontsize=11)
ax1_1.set_ylabel("(1 + 1/n)^n")
ax1_1.set_xticks(range(len(labels_e1)))
ax1_1.set_xticklabels(labels_e1, rotation=45, ha="right", fontsize=9)
ax1_1.set_ylim(1.9, 3.1)
ax1_1.grid(axis="y", linestyle=":", alpha=0.5)
ax1_1.legend(loc="lower right")

for bar in bars1:
    yval = bar.get_height()
    ax1_1.text(
        bar.get_x() + bar.get_width() / 2.0,
        yval + 0.02,
        f"{yval:.6f}",
        ha="center",
        va="bottom",
        rotation=90,
        fontsize=7,
    )

# Subplot 2: Log-scale Errors (Light Purple)
ax1_2.bar(
    range(len(labels_e1)),
    errors_e1,
    color=PURPLE_LIGHT,
    edgecolor=PURPLE_DARK,
    width=0.7,
)
ax1_2.set_yscale("log")
ax1_2.set_title("Error shrinks like e/(2n)", fontsize=11)
ax1_2.set_ylabel("| (1 + 1/n)^n - e | (log scale)")
ax1_2.set_xticks(range(len(labels_e1)))
ax1_2.set_xticklabels(labels_e1, rotation=45, ha="right", fontsize=9)
ax1_2.grid(True, which="both", linestyle=":", alpha=0.5)

plt.tight_layout()
plt.savefig("exercise1_output.png", dpi=300)
plt.close(fig1)

# ==========================================
# EXERCISE 2: (a^h - 1)/h settling to ln(a)
# ==========================================
print("Generating Exercise 2...")

h_labels_e2 = [
    "h = 0.1",
    "h = 0.01",
    "h = 0.001",
    "h = 0.0001",
    "h = 1e-05",
    "h = 1e-06",
    "h = 1e-07",
]
h_vals_e2 = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]

bases_e2 = [2, math.e, 3]
base_names_e2 = [
    f"a=2  (ln a = {math.log(2):.4f})",
    "a=e  (ln a = 1.0000)",
    f"a=3  (ln a = {math.log(3):.4f})",
]
bar_colors_e2 = [BLUE_LIGHT, PURPLE_LIGHT, PINK_LIGHT]
line_colors_e2 = [BLUE_DARK, PURPLE_DARK, PINK_DARK]

x_e2 = np.arange(len(h_labels_e2))
width_e2 = 0.25

fig2, ax2 = plt.subplots(figsize=(12, 6))
fig2.suptitle(
    "Exercise 2: (a^h - 1)/h settling to ln(a)", fontsize=14, fontweight="bold"
)
ax2.set_title(
    "Bars: difference quotient per h. Dashed lines: the limit ln(a).",
    fontsize=11,
)

for i, a in enumerate(bases_e2):
    quotients = [(a**h - 1) / h for h in h_vals_e2]
    ax2.bar(
        x_e2 + (i - 1) * width_e2,
        quotients,
        width_e2,
        label=base_names_e2[i],
        color=bar_colors_e2[i],
        edgecolor=line_colors_e2[i],
    )
    ax2.axhline(
        y=math.log(a),
        color=line_colors_e2[i],
        linestyle="--",
        linewidth=1,
        alpha=0.7,
    )

ax2.set_ylabel("(a^h - 1) / h")
ax2.set_xticks(x_e2)
ax2.set_xticklabels(h_labels_e2)
ax2.set_ylim(0.6, 1.25)
ax2.grid(axis="y", linestyle=":", alpha=0.5)
ax2.legend(loc="upper right")

plt.tight_layout()
plt.savefig("exercise2_output.png", dpi=300)
plt.close(fig2)

# ==========================================
# EXERCISE 3: e^x Taylor Series Expansion
# ==========================================
print("Generating Exercise 3...")

N_terms_e3 = [1, 2, 3, 5, 10, 15, 20, 50, 100, 1000, 10000]
x_val_e3 = 1.0

# Iterative summation avoids large integer factorial conversion errors
partial_sums_e3 = []
for N in N_terms_e3:
    current_sum = 0.0
    term = 1.0  # k = 0 term: x^0 / 0! = 1
    for k in range(N):
        if k > 0:
            term *= x_val_e3 / k
        current_sum += term
    partial_sums_e3.append(current_sum)

errors_e3 = [abs(e_exact - s) for s in partial_sums_e3]

fig3, (ax3_1, ax3_2) = plt.subplots(1, 2, figsize=(14, 6))
fig3.suptitle(
    "Exercise 3: e^x = sum x^n / n! (x = 1), summation up to N = 10,000 terms",
    fontsize=13,
    fontweight="bold",
)

# Subplot 1: Partial Sums (Light Purple)
ax3_1.bar(
    range(len(N_terms_e3)),
    partial_sums_e3,
    color=PURPLE_LIGHT,
    edgecolor=PURPLE_DARK,
    width=0.7,
)
ax3_1.axhline(
    y=e_exact,
    color=PINK_DARK,
    linestyle="--",
    label=f"e = {e_exact:.6f}",
    linewidth=1.5,
)
ax3_1.set_title("Histogram of the partial sums", fontsize=11)
ax3_1.set_ylabel("S_N = sum_{n=0..N} x^n / n!")
ax3_1.set_xlabel("number of terms N in the summation", fontsize=9)
ax3_1.set_xticks(range(len(N_terms_e3)))
ax3_1.set_xticklabels([str(n) for n in N_terms_e3], rotation=45, fontsize=8)
ax3_1.set_ylim(1.0, 3.0)
ax3_1.grid(axis="y", linestyle=":", alpha=0.5)
ax3_1.legend(loc="lower right")

for i, val in enumerate(partial_sums_e3):
    ax3_1.text(
        i,
        val + 0.03,
        f"{val:.5f}",
        ha="center",
        va="bottom",
        rotation=90,
        fontsize=6,
    )

# Subplot 2: Precision Convergence (Blue & Light Blue)
ax3_2.plot(
    range(len(N_terms_e3)),
    errors_e3,
    marker="o",
    color=BLUE_DARK,
    markerfacecolor=BLUE_LIGHT,
    linewidth=1.5,
)
ax3_2.set_yscale("log")
ax3_2.set_title("How many correct digits each N buys (log-log)", fontsize=11)
ax3_2.set_ylabel("| S_N - e | (log scale)", fontsize=9)
ax3_2.set_xlabel("number of terms N in the summation (log scale)", fontsize=9)
ax3_2.set_xticks(range(len(N_terms_e3)))
ax3_2.set_xticklabels([str(n) for n in N_terms_e3], rotation=45, fontsize=8)
ax3_2.grid(True, which="both", linestyle=":", alpha=0.5)

plt.tight_layout()
plt.savefig("exercise3_output.png", dpi=300)
plt.close(fig3)

print("All outputs generated successfully!")