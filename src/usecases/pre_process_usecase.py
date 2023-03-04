from typing import List

import pandas as pd

from configs.constants import DTYPES
from src.models.router_models import Request, InputFeatures
from src.usecases.data_validation_usecase import validate_data
from src.utils.common_utils import get_df_from_pydantic_model, timeFeatures


def pre_process_input(data: List[InputFeatures], schema) -> pd.DataFrame:
    # convert json to dataframe
    df_input = get_df_from_pydantic_model(data)

    # validate data schema
    validate_data(df_input, schema)

    df_predict = timeFeatures(df_input)

    return df_predict
