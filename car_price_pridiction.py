
#import all lib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("E:\\car.price.csv.xlsx")
#iloc ka use Pandas mein row aur column ki position (index) se data select karne ke liye hota hai. Rows → pehla : , Columns → doosra part

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
data["city-mpg"] = 235/data["city-mpg"]
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
data["length"] = data["length"] / data["length"].max()
data["width"] = data["width"] / data["width"].max()
data["height"] = data["height"] / data["height"].max()


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

print("\n")
#Convert Categorical Data to Numerical
#get_dummies()  → Categorical values ko 0 aur 1 mein convert karta hai.
data_fuel = pd.get_dummies(data["fuel-type"])
#print(data.describe())
print(data_fuel)



# Data Visualization
#Box ke bahar jo vertical line hai, usko whisker bolte hain.
plt.boxplot(data["price"])
plt.show()


sns.boxplot(x = "drive-wheels"  , y = "price" , data= data)
plt.show()

#plt.scatter()

#scatter() scatter plot banata hai.
plt.scatter(data["engine-size"] , data["price"])
plt.title("scatter plot between engine-size and price")
plt.xlabel('Engine size')
plt.ylabel('Price')
plt.grid()
plt.show()

#Grouping Data by Drive-Wheels and Body-Style
test = data[["drive-wheels" , "body-style" , "price"]]
data_grb = test.groupby(["drive-wheels" , "body-style"] ,as_index = False).mean()
print(data_grb)


print("\n")
#Create a Pivot Table & Heatmap
data_pivot = data_grb.pivot(
    index="drive-wheels",
    columns="body-style"
)

data_pivot
print(data_pivot)

plt.pcolor(data_pivot, cmap = "rainbow")
plt.colorbar()
plt.show()

'''group_annova = group_annova.groupby(["make"])
annova_result_l  =sp.stats.f_oneway(group_annova.get_group("audi" ) ["price"],
                                    group_annova.get_group("bmw")["price"],
                                    group_annova.get_group('subaru')['price'])

print(annova_results_l)

sns.regplot(x ='engine-size', y ='price', data = data)
plt.ylim(0, )'''

