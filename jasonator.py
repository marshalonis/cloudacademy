import json
import sys
import pandas as pd
import numpy as np
#from IPython.display import display

def read_and_print(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        df = pd.json_normalize(data)
        
        for index, row in df.iterrows():
            print('the name is ' + row.iloc[1])
            print('resource is ' + row.iloc[0])
        df.to_csv(sys.argv[2], index=False)
        

file_path = sys.argv[1]
read_and_print(file_path)