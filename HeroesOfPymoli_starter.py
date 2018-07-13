
# coding: utf-8

# In[ ]:


### Heroes Of Pymoli Data Analysis
* Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).

* Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
-----


# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[70]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# Raw data file
file_to_load = "Resources/purchase_data.csv"

# Read purchasing file and store into pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# ## Player Count

# * Display the total number of players
# 

# In[71]:


PlayerCount = purchase_data["SN"].nunique()
PlayerCount_disp = pd.DataFrame({"Player Count": [PlayerCount]})
PlayerCount_disp


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[72]:


Unique_Items = len(purchase_data["Item Name"].unique())
Avg_Purchase = purchase_data["Price"].mean()
Total_Purchase = len(purchase_data["Item Name"])
Revenue = purchase_data["Price"].sum()

# Create new DataFrame
Purchasing_Analysis = pd.DataFrame({"Number of Unique Items": [Unique_Items],
                                    "Average Price": [Avg_Purchase],
                                    "Number of Purchases": [Total_Purchase],
                                    "Total Revenue": [Revenue]})

# DataFrame formatting
Purchasing_Analysis["Average Price"] = Purchasing_Analysis["Average Price"].map("${:.2f}".format)
Purchasing_Analysis["Total Revenue"] = Purchasing_Analysis["Total Revenue"].map("${:.2f}".format)
Purchasing_Analysis = Purchasing_Analysis[["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"]]

Purchasing_Analysis


# ## Gender Demographics

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[26]:


duplicate = purchase_data.drop_duplicates(subset = "SN", keep = "first")
Gen_Total = duplicate["Gender"].count()
Male_Total = duplicate["Gender"].value_counts()["Male"]
Female_Total = duplicate["Gender"].value_counts()["Female"]
Non_Total = Gen_Total - Male_Total - Female_Total 

Male_Per = (Male_Total / Gen_Total) * 100
Female_Per = (Female_Total / Gen_Total) * 100 
Non_Per = (Non_Total / Gen_Total) * 100

gender_analysis = pd.DataFrame ({"": ['Male', 'Female', 'Other/Non-Disclosed'],
                            "Percentage of Players": [Male_Per, Female_Per, Non_Per],
                            "Total Count": [Male_Total, Female_Total, Non_Total]})

gender_analysis["Percentage of Players"] = gender_analysis["Percentage of Players"].map("{:.2f}%".format)
gender_analysis = gender_analysis.set_index('')
gender_analysis


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, etc. by gender
# 
# 
# * For normalized purchasing, divide total purchase value by purchase count, by gender
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[32]:


group_df = purchase_data.groupby(["Gender"])

purchase_count = group_df["SN"].count()
purchase_price = group_df["Price"].mean()
purhcase_value = group_df["Price"].sum()

duplicate = purchase_data.drop_duplicates(subset = "SN", keep = "first")
dup_group = duplicate.groupby(["Gender"])

data_norm = (group_df["Price"].sum() / group_df["SN"].count())

purchase_analysis_gen = pd.DataFrame({"Purchase Count": purchase_count,
                                      "Average Purchase Price": purchase_price,
                                      "Total Purchase Value": purhcase_value,
                                      "Normalized Totals": data_norm})

purchase_analysis_gen["Average Purchase Price"] = purchase_analysis_gen["Average Purchase Price"].map("${:.2f}".format)
purchase_analysis_gen["Total Purchase Value"] = purchase_analysis_gen["Total Purchase Value"].map("${:.2f}".format)
purchase_analysis_gen["Normalized Totals"] = purchase_analysis_gen["Normalized Totals"].map("${:.2f}".format)
purchase_analysis_gen = purchase_analysis_gen[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
purchase_analysis_gen


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[73]:


# Establish bins for ages
age_bins = [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

bins_df = purchase_data.copy()
bins_df["Age Groups"] = pd.cut(bins_df["Age"], age_bins, labels = group_names)
group_bin = bins_df.groupby(["Age Groups"])

binCount = group_bin["SN"].count()
countTotal = purchase_data["SN"].count()
percent = (binCount / countTotal) * 100
percent

age_demo= pd.DataFrame ({"Total Count": binCount,
                         "Percentage of Players": percent})
age_demo["Percentage of Players"] = age_demo["Percentage of Players"].map("{:.2f}%".format)
age_demo


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, etc. in the table below
# 
# 
# * Calculate Normalized Purchasing
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[74]:


# Binning
age_bins = [0,10,15,20,25,30,35,40,200]
group_names = ['Under 10', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', 'Over 40']

# Add bins to new dataframe and groupby
bin_df = purchase_data.copy()
bin_df["Age Groups"] = pd.cut(binning_df["Age"], age_bins, labels=group_names)
binColumn = pd.cut(bin_df["Age"], age_bins, labels=group_names)
group_bin = bin_df.groupby(["Age Groups"])

# Data Manipulation
binCount = group_bin["Age"].count()
binAver = group_bin["Price"].mean()
binTotal = group_bin["Price"].sum()

# Normalize data by deleting duplicates for new counts
binduplicate = purchase_data.drop_duplicates(subset='SN', keep="first")
binduplicate["Age Groups"] = pd.cut(binduplicate["Age"], age_bins, labels=group_names)
binduplicate = binduplicate.groupby(["Age Groups"])

binNorm = (group_bin["Price"].sum() / binduplicate["SN"].count())
binNorm

# Create new DF and format
Age_ana = pd.DataFrame({"Purchase Count": binCount,
                         "Average Purchase Price": binAver,
                         "Total Purchase Value": binTotal,
                         "Normalized Totals": binNorm})

Age_ana["Average Purchase Price"] = Age_ana["Average Purchase Price"].map("${:.2f}".format)
Age_ana["Total Purchase Value"] = Age_ana["Total Purchase Value"].map("${:.2f}".format)
Age_ana["Normalized Totals"] = Age_ana["Normalized Totals"].map("${:.2f}".format)
Age_ana = Age_Demo[["Purchase Count", "Average Purchase Price", "Total Purchase Value", "Normalized Totals"]]
Age_ana.head(10)


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[75]:


group_SN = purchase_data.groupby(["SN"])
group_Count = group_SN["Item ID"].count()
group_Total = group_SN["Price"].sum()
group_Avg = (group_Total / group_Count)

# Build DF and format
spending_ana = pd.DataFrame({"Purchase Count": group_Count,
                         "Average Purchase Price": group_Avg,
                         "Total Purchase Value": group_Total})

spending_ana = spending_ana.sort_values("Total Purchase Value", ascending=False) 
spending_ana["Average Purchase Price"] = spending_ana["Average Purchase Price"].map("${:.2f}".format)
spending_ana["Total Purchase Value"] = spending_ana["Total Purchase Value"].map("${:.2f}".format)
spending_ana = spending_ana[["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]
spending_ana.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[76]:


group_item = purchase_data.groupby(["Item ID", "Item Name"])
group_Count = group_item["SN"].count()
group_Total = group_item["Price"].sum()
group_price = (group_Total / group_Count)
group_value = (group_Total * group_Count)

# Build DF and format
pop_ana = pd.DataFrame({"Purchase Count": group_Count,
                         "Item Price": group_price,
                         "Total Purchase Value": group_value})

pop_ana = pop_ana.sort_values("Purchase Count", ascending=False)
pop_ana["Item Price"] = pop_ana["Item Price"].map("${:.2f}".format)
pop_ana["Total Purchase Value"] = pop_ana["Total Purchase Value"].map("${:.2f}".format)
pop_ana = pop_ana[["Purchase Count", "Item Price", "Total Purchase Value"]]
pop_ana.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[77]:


group_item = purchase_data.groupby(["Item ID", "Item Name"])
group_Count = group_item["Gender"].count()
group_Total = group_item["Price"].sum()
group_price = (group_Total / group_Count)

# Build DF and format
pop_ana = pd.DataFrame({"Purchase Count": group_Count,
                         "Item Price": group_price,
                         "Total Purchase Value": group_price})

pop_ana = pop_ana.sort_values("Total Purchase Value", ascending=False)
pop_ana["Item Price"] = pop_ana["Item Price"].map("${:.2f}".format)
pop_ana["Total Purchase Value"] = pop_ana["Total Purchase Value"].map("${:.2f}".format)
pop_ana = pop_ana[["Purchase Count", "Item Price", "Total Purchase Value"]]
pop_ana.head()

