# Electronic-s-Sale-Annual-Report
 * to analyze and answer the business question of electronic's sales report
 * to visualization the sales report's data
 
 ## Code and Resources Used 
  **Python Version:** 3.8  
  **Packages:** pandas, matplotlib, glob, seaborn, itertools, collections
  **Dataset:**  https://github.com/KeithGalli/Pandas-Data-Science-Tasks  
  
 ## Business Questions
  - What was the best month for sales? How much was earned that month?
  - What city sold the most product?
  - What time should we display advertisemens to maximize the likelihood of customer’s buying product?
  - What products are most often sold together?
  - What product sold the most? Why do you think it sold the most?
 
 ## Import dataset and Data Cleaning
  * Starting with import all dataset and concat those to 1 dataset for a year
  * Checking NaN values and Drop if there are NaN Value
  ![Figure 1](https://github.com/boxside/Electronic-s-Sale-Annual-Report/blob/main/Figure/missing_value.png)
  
 ## Question 1 : What was the best month for sales? How much was earned that month?
  1. Make 'Month' column from 'Order Date' column using .str to get certain string and change str to int32
  2. Make 'Revenue' column from 'Quantity Ordered' multiple by 'Price Each'
  3. Groupby 'Month' Column and summarize the revenue
  4. Visualize the Data
  ![Figure 2](https://github.com/boxside/Electronic-s-Sale-Annual-Report/blob/main/Figure/Figure_1.png)
  Result : Best Month for sales is Descember, was earned $4.613.443.000.000
 ## Question 2 : What city sold the most product?
  1. Make 'City' column from 'Order Address' column using .split and lambda function to get City
  3. Groupby 'City' Column and summarize the revenue
  4. Visualize the Data
  ![Figure 3](https://github.com/boxside/Electronic-s-Sale-Annual-Report/blob/main/Figure/Figure_2.png)
  Result : Best Sales by City is San Francisco (CA)
 ## Question 3 : What time should we display advertisemens to maximize the likelihood of customer’s buying product?
   To make us know what the time should we display ads, we must know when people would buy our product with count the order by hour,
  to get 'Hours' Column we must take hour data from order date by using .split, then plotting the hour data with count plot the result
  as follow:
  ![Figure 4](https://github.com/boxside/Electronic-s-Sale-Annual-Report/blob/main/Figure/Figure_3.png)
  Result : as the result above, we can see the peek the amount of customer that buying our product is around 11AM-1PM and 6-9PM,
  we can display advertisemens that time to maximize our sales
 ## Question 4 : What products are most often sold together?
   It's Bundling Time!, some our customers bought our products more than 1, with this condition, we can make a great deals with bundle
  that we maximize our revenue.
  1. make 'Bundle' column by group the dataset by Order ID and find Join Product with same order id
  2. drop the duplicate order id.
  3. count the product that sold together using Counter() and combinations()
  4. make new dataframe with bundle and count itself
  ![Figure 4](https://github.com/boxside/Electronic-s-Sale-Annual-Report/blob/main/Figure/Figure_5.png)
  Result : the products are most sold together are iPhone and Lightning Charging Cable, then followed by Google Phone and USB-C Charging Cable.
  with this result next year we can make new strategy with bundling discount to maximize our sales.
 ## Question 5 : What product sold the most? Why do you think it sold the most?
  1. make new dataset with groupped data by 'Product" column with summarize the quantitiy ordered
  2. make 'Price Each' column by .mean itself  
  4. Visualize the Data with 2 y-axis by quantity ordered and price each
  ![Figure 5](https://github.com/boxside/Electronic-s-Sale-Annual-Report/blob/main/Figure/Figure_4.png)
  Result : the products are most sold is AAA - Batteries (4-packs), because the aaa batteries is have more function with electronic device.
  then the price is cheap, our customer tend to buy more.
  
  
