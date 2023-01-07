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
print(df.isna().sum())
User_ID                            0
Product_ID                         0
Gender                             0
Age                                0
Occupation                         0
City_Category                      0
Stay_In_Current_City_Years         0
Marital_Status                     0
Product_Category_1                 0
Product_Category_2            173638
Product_Category_3            383247
Purchase                           0
dtype: int64
"""
data = df.dropna()
# print(data.isna().sum())

"""
print(data.select_dtypes(exclude="object").describe().T)
                    count          mean  ...        75%        max
User_ID             166821.0  1.003037e+06  ...  1004480.0  1006040.0
Occupation          166821.0  8.178886e+00  ...       14.0       20.0
Product_Category_1  166821.0  2.742766e+00  ...        4.0       15.0
Product_Category_2  166821.0  6.896871e+00  ...       10.0       16.0
Product_Category_3  166821.0  1.266824e+01  ...       16.0       18.0
Purchase            166821.0  1.165811e+04  ...    15626.0    23959.0
"""
data = data.drop(["User_ID", "Product_ID", "City_Category", "Stay_In_Current_City_Years",
                  "Marital_Status"], axis=1)


# --- Age vs Purchase ---
age = "Age"
purchase = "Purchase"
plt.figure(figsize=(10, 8))

plt.suptitle("Age vs Purchase", fontweight="bold", fontsize=16, fontfamily="sans-serif", color=black_grad[0])
sns.barplot(data=data, x=age, y=purchase)
plt.xlabel("Age", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

# --- Occupation vs Purchase ---
occupation = "Occupation"
purchase = "Purchase"

plt.figure(figsize=(12, 12))
plt.subplot(1, 2, 1)
plt.suptitle("Occupation vs Purchase", fontweight="bold", fontsize=16, fontfamily="sans-serif", color=black_grad[0])
# plt.scatter(data=data, y=purchase, x=age)
sns.barplot(data=data, x=occupation, y=purchase)
plt.xlabel("Occupation", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

plt.subplot(1, 2, 2)
plt.title("Box Plot", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(y=occupation, data=data, linewidth=1.5, color=color_mix[0])
plt.ylabel("Occupation", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

# --- Product_Category_1 vs Purchase ---
Product_Category_1 = "Product_Category_1"
purchase = "Purchase"

plt.figure(figsize=(12, 12))
plt.subplot(1, 2, 1)
plt.suptitle("Product_Category_1 vs Purchase", fontweight="bold",
             fontsize=16, fontfamily="sans-serif", color=black_grad[0])
# plt.scatter(data=data, y=purchase, x=age)
sns.barplot(data=data, x=Product_Category_1, y=purchase)
plt.xlabel("Product_Category_1", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

plt.subplot(1, 2, 2)
plt.title("Box Plot", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(y=Product_Category_1, data=data, linewidth=1.5, color=color_mix[0])
plt.ylabel("Product_Category_1", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

# --- Product_Category_2 vs Purchase ---
Product_Category_2 = "Product_Category_2"
purchase = "Purchase"

plt.figure(figsize=(12, 12))
plt.subplot(1, 2, 1)
plt.suptitle("Product_Category_2 vs Purchase", fontweight="bold", fontsize=16,
             fontfamily="sans-serif", color=black_grad[0])
sns.barplot(data=data, x=Product_Category_2, y=purchase)
plt.xlabel("Product_Category_2", fontweight="regular", fontsize=11,
           fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

plt.subplot(1, 2, 2)
plt.title("Box Plot", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(y=Product_Category_2, data=data, linewidth=1.5, color=color_mix[0])
plt.ylabel("Product_Category_2", fontweight="regular", fontsize=11,
           fontfamily="sans-serif", color=black_grad[1])

# --- Product_Category_3 vs Purchase ---
Product_Category_3 = "Product_Category_3"
purchase = "Purchase"

plt.figure(figsize=(12, 12))
plt.subplot(1, 2, 1)
plt.suptitle("Product_Category_3 vs Purchase", fontweight="bold", fontsize=16,
             fontfamily="sans-serif", color=black_grad[0])

sns.barplot(data=data, x=Product_Category_3, y=purchase)
plt.xlabel("Product_Category_2", fontweight="regular", fontsize=11,
           fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Purchase", fontweight="regular", fontsize=11, fontfamily="sans-serif", color=black_grad[1])

plt.subplot(1, 2, 2)
plt.title("Box Plot", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[1])
sns.boxplot(y=Product_Category_3, data=data, linewidth=1.5, color=color_mix[0])
plt.ylabel("Product_Category_3", fontweight="regular", fontsize=11,
           fontfamily="sans-serif", color=black_grad[1])

plt.show()
