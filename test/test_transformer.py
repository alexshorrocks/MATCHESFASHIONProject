import pandas as pd
import pytest
from pytest import mark
import numpy as np

from src.transformer import Transformer


@pytest.fixture
def order_data_instance():
    return pd.DataFrame({
        'orderId': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8'],
        'amount': ['10', '2000', '30', '40', '5000', '60', '70', '80'],
        'customer': ['Harpal', 'Kelcey',  'Augustus', 'Callum', 'Yulia', 'Brandon', 'Sam', 'Umit'],
        'date': ['2022-01-01', '2022-01-02', '2022-01-04', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08'],
    })


@pytest.fixture
def order_countries():
    return ['GBR', 'AUS', 'USA', 'GBR', 'RUS', 'GBR', 'KOR', 'NZ']


class TestTransformer:

    # Task 1
    def test__enrich_orders(self, order_data_instance):
        df = order_data_instance
        transformer = Transformer()

        enriched_orders = transformer.enrich_orders(df, 'testCol', 'testValue')

        assert np.all(enriched_orders['testCol'] == ['testValue', 'testValue', 'testValue', 'testValue', 'testValue', 'testValue', 'testValue', 'testValue'])

    # TODO: Task 2
    @mark.notimplemented
    def test__split_customers(self, order_data_instance, order_countries):
        #Here is my test, it took a few attempts, but should PASS for both parts of the df 
        transformer = Transformer()
        df = order_data_instance
        df['Country'] = order_countries
        data_instance_threshold = df['amount'].mean()
        data_instance_thresholdd = 900

        test_split_tuple = transformer.split_customers(df, data_instance_threshold)


        lower = pd.DataFrame({
        'orderId': ['M1', 'M3', 'M4', 'M6', 'M7', 'M8'],
        'amount': ['10', '30', '40', '60', '70', '80'],
        'customer': ['Harpal',  'Augustus', 'Callum', 'Brandon', 'Sam', 'Umit'],
        'date': ['2022-01-01', '2022-01-04', '2022-01-04', '2022-01-06', '2022-01-07', '2022-01-08'],
        'Country': ['GBR', 'USA', 'GBR', 'GBR', 'KOR', 'NZ']
    })
        upper = pd.DataFrame({
        'orderId': ['M2','M5'],
        'amount': ['2000', '5000'],
        'customer': ['Kelcey', 'Yulia'],
        'date': ['2022-01-02', '2022-01-05'],
        'Country': ['AUS', 'RUS'],
    })
        upper['amount'] = upper['amount'].astype(int)
        lower['amount'] = lower['amount'].astype(int)
        #Ignore below (I kept these in, in case you wanted to see my process/thinking somewhat)
        ##-----##
        #lower.astype({'amount': 'int32'}).dtypes
        #upper.astype({'amount': 'int32'}).dtypes
        #Note to self: Not sure if possible to use threshold value from the if __name__ == '__main__'
        #print(transformer.split_customers(df, data_instance_thresholdd))
        #print('----------------------------')
        #print((upper,lower))
        #print(part1)
        #print(type(upper['amount']))
        #pd.testing.assert_frame_equal(returned_value == (upper.reset_index(drop=True),lower.reset_index(drop=True)))
        ##-----##
        #Below


        (part1, part2) = transformer.split_customers(df, data_instance_thresholdd)
        pd.testing.assert_frame_equal(part1, upper)
        pd.testing.assert_frame_equal(part2, lower)
        

