from typing import Union

from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder

from src.models.router_models import Request
from src.usecases.pre_process_usecase import pre_process_input


def model_predict(body: Union[Request, UploadFile], xgboost_model):

    # pre process data
    df_predict, df_input = pre_process_input(body)

    # predict using trained model
    df_predictions = xgboost_model.predict(df_predict)
    df_input['is_attributed'] = df_predictions

    return jsonable_encoder(df_input.to_dict('records'))


def model_predict_on_file(body: UploadFile, xgboost_model):

    # pre process data
    df_predict, df_input = pre_process_input(body)

    # predict using trained model
    df_predictions = xgboost_model.predict(df_predict)
    df_input['is_attributed'] = df_predictions

    return df_input
