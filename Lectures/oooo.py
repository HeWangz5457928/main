import pandas as pd
import numpy as np

# Write this function
def mk_df(date_info, aud_usd_info, eur_aud_info):
    """ Combines the information from different sources to produce a dataframe
    with dates row labels. Row labels must be sorted

    Parameters
    ----------
    date_info : list
        date_info = [(row_id, date)]

    aud_usd_info : list
        aud_usd_info = [(row_id, aud/usd)]


    eur_aud_info : list
        eur_aud_info = [(row_id, eur/aud)]

    Returns
    -------
    df
    """

    data_info_idx, data_info_values = zip(*date_info)
    data_info_series = pd.Series(data_info_values, index=data_info_idx)

    aud_usd_idx, aud_usd_values = zip(*aud_usd_info)
    aud_usd_series = pd.Series(aud_usd_values, index=aud_usd_idx)

    eur_aud_idx, eur_aud_values = zip(*eur_aud_info)
    eur_aud_series = pd.Series(eur_aud_values, index=eur_aud_idx)


    df = pd.concat([data_info_series, aud_usd_series, eur_aud_series], axis=1)
    print(df)

    date_col = df.iloc[:,0]
    aud_usd_col = df.iloc[:,1]
    eur_aud_col = df.iloc[:,2]
    df2 = pd.concat([aud_usd_col, eur_aud_col], axis=1)
    df2.index = date_col
    df2.columns = [['AUD/USD', 'EUR/AUD']]
    df2.sort_index(inplace=True)
    df2.index.name = None

    return df2

# Sample data for you to develop your function
# date_info = [(row_id, date)]
date_info = [
    (11 , '2020-09-08'),
    (70 , '2020-09-09'),
    (99 , '2020-09-10'),
    (4  , '2020-09-11'),
    (7  , '2020-09-14'),
    (100, '2020-09-15'),
    ]

# aud_usd_info = [(row_id, aud/usd)]
aud_usd_info = [
    (70 ,  0.7209),
    (4  ,  0.7263),
    (11 ,  0.7280),
    (7  ,  0.7281),
    (100,  0.7285),
]


# eur_aud_info = [(row_id, eur/aud)]
eur_aud_info = [
    (70 ,  1.6321),
    (4  ,  1.6282),
    (99 ,  1.6221),
    (100,  1.6288),
    (11 ,  1.6232),
    ]

df = mk_df(date_info, aud_usd_info, eur_aud_info)
print(df)



