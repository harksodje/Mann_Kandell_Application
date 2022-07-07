import pandas as pd


def mk_test(data: dict, method, type: str)-> pd.DataFrame:
    res = {}
    for i, j in data.items():
        res[i] = method(j)[:]
    df_res = pd.DataFrame(res, index=['trend', 'h', 'p', 'z', 'Tau', 's', 'var_s', 'slope', 'intercept']).T
    print(f"The result of {type} mann-kendall trend model")
    return df_res


def convert_df_to_dict(df: pd.DataFrame) -> dict:
    df_columns = df.columns.to_list()
    data = dict() 
    for i in range(0, len(df_columns)):
        
        data[df_columns[i]] = df.iloc[: , i].to_numpy()
    return data
