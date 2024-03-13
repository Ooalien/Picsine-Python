import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''Load a csv file into a pandas dataframe'''
    data = pd.read_csv(path)
    print(f"Loading dataset of dimensions {data.shape}")
    return data
