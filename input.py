import pandas as pd


def read_sample_dataset():
    return pd.read_csv('data/eleicoes-twitter-small.csv', delimiter=';')

def read_full_dataset():
    return pd.read_csv('data/eleicoes-twitter.csv', delimiter=';')
