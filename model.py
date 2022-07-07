# import libaries
import pandas as pd
from helpers import convert_df_to_dict

# data path
path = 'C:/Users/user/Desktop/demo_first/Mann_Kandell_Application/data/computed_erosivity.csv'
df = pd.read_csv(path, index_col='Months')

# data conversion
data = convert_df_to_dict(df)
