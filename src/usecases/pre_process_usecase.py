from typing import Union

import pandas as pd
from fastapi import UploadFile

from configs.constants import DATETIME_COLUMN
from src.models.router_models import Request
from src.utils.common_utils import get_df_from_pydantic_model, timeFeatures


def pre_process_input(body: Union[Request, UploadFile]) -> [pd.DataFrame, pd.DataFrame]:
    try:
        data = body.input_data

        # convert json to dataframe
        df_input = get_df_from_pydantic_model(data)
    except:
        df_input = pd.read_csv(body.file)
        if DATETIME_COLUMN in df_input.columns.tolist():
            df_input[DATETIME_COLUMN] = pd.to_datetime(df_input[DATETIME_COLUMN])
        body.file.close()

    df_predict = df_input.copy()
    df_predict = timeFeatures(df_predict)

    return df_predict, df_input
