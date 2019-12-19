import sys
import datetime
import pickle

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.multiclass import OneVsOneClassifier


def classify(f, verbose=True):
    """
    Function that takes as input a csv file containing a list of transactions
    and returns the list of clients along with the cluster they belong to.

    :param f: Path of the file containing the transactions
    :param verbose: If True, will show the result of the classification
    :return: List of clients, with their cluster group
    """
    df = pd.read_csv(f, sep=';')
    df['Price'] = df['Quantity'] * df['UnitPrice']
    df['InvoiceDate'] = df['InvoiceDate'].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y'))
    df['Cancelled'] = df['InvoiceNo'].astype(str).str.startswith('C')

    # Functions useful to create the clients table
    def first(x): return (datetime.datetime(2011, 12, 10) - x.min()).days
    def last(x): return (datetime.datetime(2011, 12, 10) - x.max()).days
    def unique(x): return len(x.unique())
    def cancel_rate(x): return x.sum() / (len(x) - x.sum())

    # Add recency, days since first transaction and number of transactions (frequency)
    temp = df[~df.Cancelled]
    customers = temp.groupby('CustomerID').agg({
        'InvoiceDate': [last, first],
        'InvoiceNo': unique,
    })
    customers.columns = ['_'.join(x) for x in customers.columns.ravel()]
    customers.rename(columns={'InvoiceDate_last': 'recency', 'InvoiceDate_first': 'client_since',
                              'InvoiceNo_unique': 'frequency'}, inplace=True)
    # Add mean quantity, total revenue and cancel rate
    temp = df.groupby('CustomerID').agg({
        'Quantity': 'mean',
        'Price': lambda x: x.sum(),
        'Cancelled': cancel_rate,
    })
    customers = pd.merge(customers, temp, left_index=True, right_index=True)
    customers.rename(columns={'Quantity': 'quantity_mean', 'Price': 'monetary_value',
                              'Cancelled': 'cancel_rate'}, inplace=True)
    customers = customers[(customers.monetary_value >= 1)]

    # Loading parameters
    with open('params.pickle', 'rb') as f:
        params = pickle.load(f)

    std_scaler = StandardScaler()
    std_scaler.mean_ = params['mean_']
    std_scaler.var_ = params['var_']
    std_scaler.scale_ = params['scale_']

    lr = OneVsOneClassifier(params['estimator'])
    lr.estimators_ = params['estimators_']
    lr.classes_ = params['classes_']
    lr.pairwise_indices_ = None

    customers_std = std_scaler.transform(customers)
    y_pred = lr.predict(customers_std)

    temp = customers.copy()
    temp['cluster'] = y_pred
    temp['cluster_name'] = temp['cluster'].apply(lambda x: params['class_names'][x])

    if verbose:
        print(temp['cluster_name'])

    return temp['cluster_name']


if __name__ == '__main__':
    classify(sys.argv[1])
