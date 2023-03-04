import gc
from typing import Union

from fastapi import File, UploadFile

from src.models.router_models import Request
from src.usecases.pre_process_usecase import pre_process_input
from fastapi.encoders import jsonable_encoder


def model_predict(body: Union[Request, UploadFile], xgboost_model, schema):

    # pre process data
    df_predict, df_input = pre_process_input(body, schema)

    # predict using trained model
    df_predictions = xgboost_model.predict(df_predict)

    return jsonable_encoder(df_predictions.to_dict('records'))


def model_predict_on_file(body: UploadFile, xgboost_model, schema):

    # pre process data
    df_predict, df_input = pre_process_input(body, schema)

    # predict using trained model
    df_predictions = xgboost_model.predict(df_predict)
    df_input['is_attributed'] = df_predictions

    return df_input
