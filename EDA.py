import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from yellowbrick import set_palette
import warnings

# ---Libraries Settings ---
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 100
set_palette("dark")
warnings.filterwarnings("ignore")

# --- Create List of Color Palettes ---
red_grad = ['#FF0000', '#BF0000', '#800000', '#400000', '#000000']
pink_grad = ['#8A0030', '#BA1141', '#FF5C8A', '#FF99B9', '#FFDEEB']
purple_grad = ['#4C0028', '#7F0043', '#8E004C', '#A80059', '#C10067']
color_mix = ['#F38BB2', '#FFB9CF', '#FFD7D7', '#F17881', '#E7525B', "#C10067", "#A80059"]
black_grad = ['#100C07', '#3E3B39', '#6D6A6A', '#9B9A9C', '#CAC9CD']

df = pd.read_csv("train.csv")
"""
print(df.columns)
Index(['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category',
       'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
       'Product_Category_2', 'Product_Category_3', 'Purchase'])

"""
data = df.dropna()

mean = data.groupby("Gender")["Purchase"].mean()
"""
Gender
F    11084.723786
M    11824.922756
Name: Purchase, dtype: float64 Gender
"""
median = data.groupby("Gender")["Purchase"].median()
"""
Gender
F    11428.0
M    11829.0
Name: Purchase, dtype: float64
"""
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.title("Gender EDA", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(x=data.Gender, y=data.Purchase, linewidth=1.5, color=color_mix[0])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.subplot(2, 2, 2)
plt.title("Age EDA", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(x=data.Age, y=data.Purchase, linewidth=1.5, color=color_mix[0])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.subplot(2, 2, 3)
plt.title("Occupation EDA", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(x=data.Occupation, y=data.Purchase, linewidth=1.5, color=color_mix[0])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.subplot(2, 2, 4)
plt.title("Marital_Status EDA", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(x=data.Marital_Status, y=data.Purchase, linewidth=1.5, color=color_mix[0])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])


plt.show()