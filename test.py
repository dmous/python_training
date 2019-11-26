import pandas as pd

test = pd.read_csv(r"Z:\Darshan\People\Chris\amazon_limit2019.csv", sep=";", low_memory=False)
test.info()