import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load dataset
df = pd.read_csv("customer_churn.csv")
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")  # blanks -> NaN
print(df.head())
df.info()
print(df.columns)

# Descriptive statistics
num = df.select_dtypes(include="number")
print(num.describe())
for c in num.columns:
    print(c, "| Mean:", num[c].mean(), "| Median:", num[c].median(),
          "| Mode:", num[c].mode()[0], "| Std:", num[c].std(),
          "| Var:", num[c].var(), "| Min:", num[c].min(), "| Max:", num[c].max())
    print(num[c].quantile([0.25, 0.5, 0.75]))

# Visualization
plt.hist(df['MonthlyCharges'], bins=20, edgecolor='black')
plt.title('MonthlyCharges Distribution'); plt.xlabel('MonthlyCharges'); plt.ylabel('Frequency')
plt.show()

sns.boxplot(y=df['MonthlyCharges'])
plt.title('Box Plot of MonthlyCharges')
plt.show()

plt.scatter(df['tenure'], df['MonthlyCharges'])
plt.title('Tenure vs MonthlyCharges'); plt.xlabel('tenure'); plt.ylabel('MonthlyCharges')
plt.show()

corr_matrix = num.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Handling missing data
print(df.isnull().sum())
df_dropped = df.dropna()                                # option 1: remove
df[num.columns] = df[num.columns].fillna(df[num.columns].mean())   # option 2: fill with mean
print(df.isnull().sum())

# Handling outliers (z-score)
for c in num.columns:
    df[c + '_zscore'] = zscore(df[c])
zcols = [c + '_zscore' for c in num.columns]
print(df[(df[zcols].abs() > 3).any(axis=1)])            # detected outliers

# Option 1: remove outliers
df_no_outliers = df[(df[zcols].abs() <= 3).all(axis=1)]

# Option 2: cap outliers
def cap_values(series):
    upper_limit = series.mean() + 3*series.std()
    lower_limit = series.mean() - 3*series.std()
    return series.clip(lower=lower_limit, upper=upper_limit)

df_capped = df.copy()
for c in num.columns:
    df_capped[c] = cap_values(df[c])

# Verify and save
print(df_no_outliers.isnull().sum())
df_no_outliers.drop(columns=zcols).to_csv("customer_churn_cleaned.csv", index=False)