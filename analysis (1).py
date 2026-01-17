import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# 1️⃣ LOAD & MERGE DATA
# =============================
files = [
    "api_data_aadhar_enrolment_0_500000.csv",
    "api_data_aadhar_enrolment_500000_1000000.csv",
    "api_data_aadhar_enrolment_1000000_1006029.csv"
]

df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
print("Total records:", len(df))

# Clean data
df = df.dropna()
df.columns = df.columns.str.lower().str.replace(" ", "_")

# =============================
# 2️⃣ TOTAL ENROLMENT COLUMN
# =============================
df["total_enrolment"] = (
    df["age_0_5"] +
    df["age_5_17"] +
    df["age_18_greater"]
)

# =============================
# 3️⃣ STATE-WISE ANALYSIS (BAR)
# =============================
state_data = (
    df.groupby("state")["total_enrolment"]
    .sum()
    .sort_values(ascending=False)
)

state_data.head(10).plot(kind="bar", figsize=(10,5))
plt.title("Top 10 States by Aadhaar Enrolment")
plt.xlabel("State")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.show()

# =============================
# 4️⃣ AGE GROUP DISTRIBUTION (PIE)
# =============================
age_distribution = df[["age_0_5", "age_5_17", "age_18_greater"]].sum()

age_distribution.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(6,6)
)
plt.title("Aadhaar Enrolment Distribution by Age Group")
plt.ylabel("")
plt.show()

# =============================
# 5️⃣ YEAR-WISE TREND (BAR CHART)
# =============================

df["year"] = pd.to_datetime(df["date"], dayfirst=True).dt.year

year_data = df.groupby("year")["total_enrolment"].sum()

year_data.plot(
    kind="bar",
    figsize=(8,5)
)

plt.title("Year-wise Aadhaar Enrolment (Bar Chart)")
plt.xlabel("Year")
plt.ylabel("Total Enrolments")
plt.tight_layout()
plt.show()


# =============================
# 6️⃣ STATE vs YEAR (BAR CHART)
# =============================

top_states = (
    df.groupby("state")["total_enrolment"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index
)

state_year_data = (
    df[df["state"].isin(top_states)]
    .groupby(["year", "state"])["total_enrolment"]
    .sum()
    .unstack()
)

state_year_data.plot(
    kind="bar",
    figsize=(10,6)
)

plt.title("State-wise Aadhaar Enrolment over Years (Bar Chart)")
plt.xlabel("Year")
plt.ylabel("Total Enrolments")
plt.legend(title="State")
plt.tight_layout()
plt.show()
