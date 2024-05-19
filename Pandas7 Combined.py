# Pandas7

# 1 Problem 1 : Immediate Food Delivery I ( https://leetcode.com/problems/immediate-food-delivery-i/ )

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    df = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']]
    return pd.DataFrame([round(len(df)/len(delivery)*100,2)], columns=['immediate_percentage'])

# 2 Problem 2 : Count Salary Categories  ( https://leetcode.com/problems/count-salary-categories/ ) 

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts['income'] < 20000]
    avg = accounts[(accounts['income']>= 20000) & (accounts['income']<= 50000)]
    high = accounts[accounts['income']>50000]   
    return pd.DataFrame([['Low Salary', len(low)],['Average Salary',len(avg)],['High Salary',len(high)]],columns = ['category','accounts_count'])