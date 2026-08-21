
#import all lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("E:\\car.price.csv.xlsx")
#iloc ka use Pandas mein row aur column ki position (index) se data select karne ke liye hota hai. Rows → pehla : , Columns → doosra part
df = df.iloc[ : , :]
print(df.head())

#Assign Column Headers
headers = ["symboling", "normalized-losses", "make", 
           "fuel-type", "aspiration","num-of-doors",
           "body-style","drive-wheels", "engine-location",
           "wheel-base","length", "width","height", "curb-weight",
           "engine-type","num-of-cylinders", "engine-size", 
           "fuel-system","bore","stroke", "compression-ratio",
           "horsepower", "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
print(df.head())

#Check for Missing Values
data = df
print(data.isna().any())
print(data.isna().sum())
#data.isnull().any() is work same is above line of code


#Convert MPG to L/100km
data["city-mpg"] = 235/df["city-mpg"]
data.rename(columns = {"city-mpg" : "city-l / 100km"} , inplace = True)
print(data.columns)
print(data.dtypes)


# Convert Price Column ke kitne unique values hai
unique_price = data.price.unique()
print(unique_price)

print("\n")

#check kitni unique walue mai ? hai 
data = data[data.price != "?"]
print(data.price)
print("\n")

print("?" in data.price.unique())
print("\n")

#convert into interger
data["price"] = data["price"].astype(int)
print(data["price"].dtypes)


#Normalize Features
length_nor =data["length"] = data["length"] / data["length"].max()
width_nor =data["width"] = data["width"] / data["width"].max()
height_nor= data["height"] = data["height"] / data["height"].max()

#3 parts mai price ko divide karna
bins = np.linspace(data["price"].min(), data["price"].max(), 4)
#print(bins)
group_names = ["low", "medium" , "high"]
data["price_binned"] = pd.cut(data["price"] , bins , labels = group_names, include_lowest = True) 
print(data["price_binned"])
#visual graph
plt.hist(data["price_binned"])
plt.show()
#secand method


data['price_binned'].value_counts().plot(kind='bar')
plt.show()

#Convert Categorical Data to Numerical
data = pd.get_dummies(data["fuel-type"])
print(data)