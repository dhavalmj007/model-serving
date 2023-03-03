from typing import List

import pandas as pd
from pydantic import BaseModel


def get_df_from_pydantic_model(data: List[BaseModel]) -> pd.DataFrame:
    df = pd.DataFrame([s.__dict__ for s in data])

    return df


def timeFeatures(df):
    # Make some new features with click_time column
    df['datetime'] = pd.to_datetime(df['click_time'])
    df['dow'] = df['datetime'].dt.dayofweek
    df["doy"] = df["datetime"].dt.dayofyear
    # df["dteom"]    = df["datetime"].dt.daysinmonth - df["datetime"].dt.day
    df.drop(['click_time', 'datetime'], axis=1, inplace=True)
    return df
