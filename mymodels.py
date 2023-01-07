import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from yellowbrick import set_palette
import warnings
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score

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
df.drop(["User_ID", "Product_ID", "City_Category"], axis=1, inplace=True)

# # --- Data Preprocessing ---
df["Gender"] = df["Gender"].map({"F": 0, "M": 1}) #.astype(int).where((df.Gender > 1.0) & (df.Gender < 2.0))

# Q1 = np.percentile(df.Gender, 25, interpolation="midpoint").reshape(-1, 1)
# Q3 = np.percentile(df.Gender, 75, interpolation="midpoint").reshape(-1, 1)
# IQR = Q3 -Q1
# upper = np.where(df.Gender > (Q3+1.5*IQR))
# lower = np.where(df.Gender < (Q1-1.5*IQR))
# df.drop(upper, inplace=True)
# df.drop(lower, inplace=True)
# sns.boxplot(df.Gender)


df["Age"] = df["Age"].map({"0-17": 1, "18-25": 2, "26-35": 3, "36-45": 4, "46-50": 5,
                           "51-55": 6, "55+": 7})

# sns.boxplot(df.Age)
# print(df.isnull().sum())

df["Product_Category_2"] = df["Product_Category_2"].fillna(df["Product_Category_2"].mode()[0])
df["Product_Category_3"] = df["Product_Category_3"].fillna(df["Product_Category_3"].mode()[0])
df["Stay_In_Current_City_Years"] = df["Stay_In_Current_City_Years"].str.replace("+", "")
df["Stay_In_Current_City_Years"] = df["Stay_In_Current_City_Years"].astype(int)

sns.heatmap(df.corr(), cmap="Reds", annot=True)

print(df.isnull().sum())
print(df.info())

X = df.drop(["Purchase"], axis=1)
y = df["Purchase"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = DecisionTreeRegressor(random_state=1)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test).round()
accuracy = accuracy_score(y_pred, y_test)
print(".:. Decision Tree Regressor:"+"\033[1m {:.2f}%".format(accuracy*100)+".:.")
plt.show()