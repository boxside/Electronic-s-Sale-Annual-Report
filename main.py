# import library

import pandas as pd
import matplotlib.pyplot as plt
import glob
import seaborn as sns
from itertools import  combinations
from collections import Counter

#import dataset
path =r'C:\Users\fikri\Desktop\pyproj\sales_electronic\Sales_Data'
filenames = glob.glob(path + "\*.csv")

dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
all_data = pd.concat(dfs, ignore_index=True)

print(all_data.head())

#checking null value

def display_missing(df):
    for col in df.columns.tolist():
        print('{} column missing values: {}'.format(col, df[col].isnull().sum()))
    print('\n')

for df in dfs:
    print('{}'.format(df))
    display_missing(all_data)

clean_df= all_data.dropna(how='all')




# make 'Month' column from order date using .str
clean_df= clean_df[clean_df['Order Date'].str[0:2] !='Or']


clean_df['Month'] = clean_df['Order Date'].str[0:2]
clean_df['Month'] = clean_df['Month'].astype('int32')

# add Revenue Column
clean_df['Quantity Ordered'] = clean_df['Quantity Ordered'].astype('int32')
clean_df['Price Each'] = clean_df['Price Each'].astype('float')
clean_df['Revenue'] = clean_df['Quantity Ordered'] * clean_df['Price Each']
Revenue_sum = clean_df.groupby('Month').sum()
print(Revenue_sum)
Revenue_sum['Month'] = Revenue_sum.index

                ### Question 1 :What was the best month for sales? How much was earned that month? ###
plt.rcParams['figure.figsize']=(20, 30)
plt.style.use('dark_background')

sns.catplot(x='Month', y='Revenue', data=Revenue_sum,palette = 'crest', kind='bar', legend=True)
plt.xlabel('Month', size=10, labelpad=20)
plt.ylabel('Revenue ($)', size=10, labelpad=20)
plt.title('Best Sales by Month', fontweight = 30, fontsize = 20)
plt.xticks( fontsize=12)

# get city from purchse address
def city(address):
    return address.split(',')[1]
def state(address):
    return address.split(',')[2].split(' ')[1]

clean_df['City'] = clean_df['Purchase Address'].apply(lambda x : f" {city(x)} ({state(x)})")

City_sum = clean_df.groupby('City').sum()
City_sum['City'] = City_sum.index

                                ### Question 2 : What city sold the most product? ###
plt.rcParams['figure.figsize']=(20, 30)
plt.style.use('dark_background')

sns.catplot(x='City', y='Revenue', data=City_sum,palette = 'gnuplot', kind='bar', legend=True)
plt.xlabel('City (State)', size=10, labelpad=20)
plt.ylabel('Revenue($)', size=10, labelpad=20)
plt.title('Best Sales by City', fontweight = 30, fontsize = 20)
plt.xticks(rotation = 90, fontsize=12)
plt.show()

# get hours time from order date
def houru(time):
    return time.split(' ')[1]
clean_df['Hours'] = clean_df['Order Date'].apply(lambda x : f"{houru(x)}")
clean_df['Hours'] = clean_df['Hours'].str[0:2].astype('int32')

 ### Question 3 : What time should we display advertisemens to maximize the likelihood of customer’s buying product? ###
sns.countplot(x='Hours', data=clean_df)
plt.xlabel('Hours', size=10, labelpad=20)
plt.ylabel('The Number of Product Sold', size=10, labelpad=20)
plt.title('Most Product Sold by Time(Hours)', fontweight = 30, fontsize = 20)
plt.xticks( fontsize=12)
plt.show()


                            ### Question 4 : What products are most often sold together? ###
group_prod = clean_df[clean_df['Order ID'].duplicated(keep=False)]
group_prod['Bundle'] = group_prod.groupby('Order ID')['Product'].transform(lambda x : ','.join(x))
group_prod = group_prod[['Order ID', 'Bundle']].drop_duplicates()
print(group_prod.head())

count = Counter()
for row in group_prod['Bundle']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

countee = pd.DataFrame(count.items(), columns=['Bundle','Count'])
countee = countee.sort_values('Count', ascending=False)
print(countee.head())


                        ### Question 5 : What product sold the most? Why do you think it sold the most? ###
product_group = clean_df.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
prod_sold = [product for product, df in product_group]
prices = clean_df.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.bar(prod_sold, quantity_ordered, color='b')
ax2.plot(prod_sold, prices, color='r')

plt.title('The Most Sold Product', fontweight = 30, fontsize = 20)
ax1.set_xlabel('Product Name', size=12)
ax1.set_ylabel('Quantity Ordered', color='b', size=12)
ax2.set_ylabel('Price Each ($)', color='r', size=12)
ax1.set_xticklabels(prod_sold, rotation='vertical', size=8)
plt.show()

