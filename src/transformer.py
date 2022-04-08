from typing import (
    List,
    Tuple,
)

import pandas as pd


#Please find my solution below, along with the split_customer test in the test_transformer.py
#Enjoyed the challenge! Also, I left some of my past attempts in so you can see my thinking.


class Transformer:

    def __init__(self):
        self

    def read_orders(self) -> pd.DataFrame:
        orders = pd.read_csv('orders.csv', header=0)
        return orders

    def enrich_orders(self, orders: pd.DataFrame, col_name: str, value: List[str]) -> pd.DataFrame:
        """
        Adds a column to the data frame

        Args:
            orders (pd.Dataframe): The dataframe to be enriched
            col_name (str): Name of the new enriched column
            value (List[str]): Data to go into the new column

        Returns:
            The enriched dataframe
        """
        #Adding new column to dataframe

        orders[col_name] = value
        return orders

    def split_customers(self, orders: pd.DataFrame, threshold: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Splits customers into two groups based on a threshold

        Args:
            orders (pd.DataFrame): The dataframe to be split
            threshold (int): Value to split the customer base on

        Returns:
            Tuple containing the split dataframes
        """

        #This should work


        orders['amount'] = orders['amount'].astype(int)

        above_threshold = orders[orders['amount'] >= threshold]
        above_threshold.reset_index(drop=True, inplace=True)
        below_threshold = orders[orders['amount'] < threshold]
        below_threshold.reset_index(drop=True, inplace=True)
        return (above_threshold, below_threshold)

        

    def bonus_task(orders):

        #This is a function to solve the bonus task questions, by returning the answers in a DataFrame. 
        
        #Change the date format to a Pythonic one
        
        orders['date'] = orders['date'].str.replace('/','-')

        max_amount = orders['amount'].max() #Find max order amount
        max_amount_name = orders[orders['amount']==max_amount]['customer'] #And the name that falls upon
        
        min_amount = orders['amount'].min() #Likewise for the minimum
        min_amount_name = orders[orders['amount']==min_amount]['customer']
        
        average_order_amount = orders['amount'].mean() #Average
        
        earliest_order_date = orders['date'].min() #And likewise for the order date
        earliest_order_date_name = orders[orders['date']==earliest_order_date]['customer']

        orders['Month'] = pd.DatetimeIndex(orders['date']).month #Creating a column for the Month to make things a bit easier to find the modal month
        #most_frequent_month = []
        #most_frequent_month.append() = orders['Month'].mode()
        
        most_frequent_month = orders['Month'].value_counts().idxmax()

        #Returning all of this in a Dataframe with a single row

        bonus_df = pd.DataFrame({'Highest Paying Customer': [max_amount_name.item()],
        'Lowest Paying Customer': [min_amount_name.item()],
        'Average Order Amount': [average_order_amount],
        'Earliest Customer': [earliest_order_date_name.item()],
        'Modal Month': [most_frequent_month.item()],
        })
        return bonus_df



if __name__ == '__main__':
    transformer = Transformer()
    data = transformer.read_orders()

    countries = ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']
    data = transformer.enrich_orders(data, 'Country', countries)

    threshold = data['amount'].mean()  # Change this value
    #The mean can be used as a cut-off threshold of high/low. In reality, a bucketing method
    #...may be more effective, however.
    low_spending_customers, high_spending_customers = transformer.split_customers(data, threshold)



