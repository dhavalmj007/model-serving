from typing import List

import pandas as pd

from configs.constants import DTYPES
from src.models.router_models import Request, InputFeatures
from src.utils.common_utils import get_df_from_pydantic_model, timeFeatures


def pre_process_input(data: List[InputFeatures]) -> pd.DataFrame:
    # convert json to dataframe
    df_input = get_df_from_pydantic_model(data)

    df_predict = timeFeatures(df_input)

    return df_predict
