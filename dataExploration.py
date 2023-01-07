import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import seaborn as sns
from yellowbrick import set_palette

# ---Libraries Settings ---
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 100
set_palette("dark")

# --- Create List of Color Palettes ---
red_grad = ['#FF0000', '#BF0000', '#800000', '#400000', '#000000']
pink_grad = ['#8A0030', '#BA1141', '#FF5C8A', '#FF99B9', '#FFDEEB']
purple_grad = ['#4C0028', '#7F0043', '#8E004C', '#A80059', '#C10067']
color_mix = ['#F38BB2', '#FFB9CF', '#FFD7D7', '#F17881', '#E7525B', "#C10067", "#A80059"]
black_grad = ['#100C07', '#3E3B39', '#6D6A6A', '#9B9A9C', '#CAC9CD']

data = pd.read_csv("train.csv")
# print(df.isnull().sum())
# data = df.dropna()
# print(data.isnull().sum())

"""
print(data.info())
RangeIndex: 550068 entries, 0 to 550067
Data columns (total 12 columns):
 #   Column                      Non-Null Count   Dtype  
---  ------                      --------------   -----  
 0   User_ID                     550068 non-null  int64  
 1   Product_ID                  550068 non-null  object 
 2   Gender                      550068 non-null  object 
 3   Age                         550068 non-null  object 
 4   Occupation                  550068 non-null  int64  
 5   City_Category               550068 non-null  object 
 6   Stay_In_Current_City_Years  550068 non-null  object 
 7   Marital_Status              550068 non-null  int64  
 8   Product_Category_1          550068 non-null  int64  
 9   Product_Category_2          376430 non-null  float64
 10  Product_Category_3          166821 non-null  float64
 11  Purchase                    550068 non-null  int64  
dtypes: float64(2), int64(5), object(5)
"""
"""
print(df.columns)
Index(['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category',
       'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
       'Product_Category_2', 'Product_Category_3', 'Purchase'])

"""
# # --- Gender ---

colors = color_mix[2:4]
labels = ["M", "F"]
order = data["Gender"].value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Sex (Gender) Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Pie Chart
plt.subplot(1, 2, 1)
plt.title("Pie Chart", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
plt.pie(data["Gender"].value_counts(), labels=labels, colors=colors, pctdistance=0.7,
        autopct="%.2f%%", wedgeprops=dict(alpha=0.8, edgecolor=black_grad[1]))
centre = plt.Circle((0, 0), 0.45, fc="white", edgecolor=black_grad[1])
plt.gcf().gca().add_artist(centre)

#  Histogram
plt.subplot(1, 2, 2)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Gender", data=data, palette=colors, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))
plt.xlabel("Gender", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.xticks([0, 1], labels)
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Sex (Gender) total :."+"\033[0m")
print("*" * 25)
print(data["Gender"].value_counts())

# --- Age ---

colors = color_mix[:]
labels = ["26-35", "36-45", "18-25", "46-50", "51-55", "55+", "0-17"]
order = data["Age"].value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Age Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Pie Chart
plt.subplot(1, 2, 1)
plt.title("Pie Chart", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
plt.pie(data["Age"].value_counts(), labels=labels, colors=colors, pctdistance=0.7,
        autopct="%.2f%%", wedgeprops=dict(alpha=0.8, edgecolor=black_grad[1]))
centre = plt.Circle((0, 0), 0.45, fc="white", edgecolor=black_grad[1])
plt.gcf().gca().add_artist(centre)

# Histogram
plt.subplot(1, 2, 2)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Age", data=data, palette=colors, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))

plt.xlabel("Age", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Age total :."+"\033[0m")
print("*" * 25)
print(data["Age"].value_counts())

# --- Occupation ---

# print(data.Occupation.unique())
# Histogram
# colors = color_mix[:]
# labels = [10, 16, 15,  7, 20,  9,  1, 12, 17,  0,  3,  4, 11,  8, 19,  2, 18,  5, 14, 13,  6]
order = data.Occupation.value_counts().index
plt.subplot(1, 1, 1)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Occupation", data=data, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=8, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))

plt.xlabel("Occupation", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Occupation total :."+"\033[0m")
print("*" * 25)
print(data["Occupation"].value_counts())


# # --- City_Category ---
# print(data.City_Category.unique())
colors = color_mix[1:4]
labels = ["B", "C", "A"]
order = data.City_Category.value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("City Category Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Pie Chart
plt.subplot(1, 2, 1)
plt.title("Pie Chart", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
plt.pie(data["City_Category"].value_counts(), labels=labels, colors=colors, pctdistance=0.7,
        autopct="%.2f%%", wedgeprops=dict(alpha=0.8, edgecolor=black_grad[1]))
centre = plt.Circle((0, 0), 0.45, fc="white", edgecolor=black_grad[1])
plt.gcf().gca().add_artist(centre)

# Histogram
plt.subplot(1, 2, 2)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="City_Category", data=data, palette=colors, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))
plt.xlabel("City Category", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: City Category total :."+"\033[0m")
print("*" * 25)
print(data["City_Category"].value_counts())

# --- Stay_In_Current_City_Years ---
print(data.Stay_In_Current_City_Years.unique())
colors = color_mix[0:6]
labels = ['1', '2', '3', '4+', '0']
order = data.Stay_In_Current_City_Years.value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Stay_In_Current_City_Years Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Pie Chart
plt.subplot(1, 2, 1)
plt.title("Pie Chart", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
plt.pie(data["Stay_In_Current_City_Years"].value_counts(), labels=labels, colors=colors, pctdistance=0.7,
        autopct="%.2f%%", wedgeprops=dict(alpha=0.8, edgecolor=black_grad[1]))
centre = plt.Circle((0, 0), 0.45, fc="white", edgecolor=black_grad[1])
plt.gcf().gca().add_artist(centre)

# Histogram
plt.subplot(1, 2, 2)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Stay_In_Current_City_Years",
                   data=data, palette=colors, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))
plt.xlabel("Stay_In_Current_City_Years", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)
print("*" * 25)
print("\033[1m"+".: Stay_In_Current_City_Years total :."+"\033[0m")
print("*" * 25)
print(data["Stay_In_Current_City_Years"].value_counts())

# --- Marital_Status ---
print(data.Marital_Status.unique())
colors = color_mix[0:2]
labels = ['0', '1']
order = data.Marital_Status.value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Marital_Status Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Pie Chart
plt.subplot(1, 2, 1)
plt.title("Pie Chart", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
plt.pie(data["Marital_Status"].value_counts(), labels=labels, colors=colors, pctdistance=0.7,
        autopct="%.2f%%", wedgeprops=dict(alpha=0.8, edgecolor=black_grad[1]))
centre = plt.Circle((0, 0), 0.45, fc="white", edgecolor=black_grad[1])
plt.gcf().gca().add_artist(centre)

# Histogram
plt.subplot(1, 2, 2)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Marital_Status", data=data, palette=colors, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))
plt.xlabel("Marital_Status", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Marital_Status total :."+"\033[0m")
print("*" * 25)
print(data["Marital_Status"].value_counts())

# --- Product_Category_1 ---
print(data.Product_Category_1.unique())
order = data.Product_Category_1.value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Product_Category_1 Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Histogram
plt.subplot(1, 1, 1)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Product_Category_1", data=data, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))
plt.xlabel("Product_Category_1", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Product_Category_1 total :."+"\033[0m")
print("*" * 25)
print(data["Product_Category_1"].value_counts())

# --- Product_Category_2 ---
data.Product_Category_2.unique()
order = data.Product_Category_2.value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Product_Category_2 Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Histogram
plt.subplot(1, 1, 1)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Product_Category_2", data=data, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))
plt.xlabel("Product_Category_2", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Product_Category_2 total :."+"\033[0m")
print("*" * 25)
print(data["Product_Category_2"].value_counts())

# #  --- Product_Category_3 ---
# print(data.Product_Category_3.unique())
order = data.Product_Category_3.value_counts().index

# Figure Size
plt.figure(figsize=(16, 8))
plt.suptitle("Product_Category_3 Distribution", fontsize=16, fontweight="heavy",
             color=black_grad[0], fontfamily="sans-serif")
# Histogram
plt.subplot(1, 1, 1)
plt.title("Histogram", fontweight="bold", fontsize=14, fontfamily="sans-serif", color=black_grad[0])
ax = sns.countplot(x="Product_Category_3", data=data, order=order, edgecolor=black_grad[2], alpha=0.85)

for rect in ax.patches:
    ax.text(rect.get_x() + rect.get_width()/2, rect.get_height()+4, rect.get_height(),
            horizontalalignment="center", fontsize=10, bbox=dict(facecolor="none",
            edgecolor=black_grad[0], linewidth=0.2, boxstyle="round"))

plt.xlabel("Product_Category_3", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.ylabel("Total", fontweight="bold", fontsize=11, fontfamily="sans-serif", color=black_grad[1])
plt.grid(axis="y", alpha=0.4)

# --- Count Categorical Labels ---
print("*" * 25)
print("\033[1m"+".: Product_Category_3 total :."+"\033[0m")
print("*" * 25)
print(data["Product_Category_3"].value_counts())


plt.show()
