import gc

from src.models.router_models import Request
from src.usecases.pre_process_usecase import pre_process_input
from fastapi.encoders import jsonable_encoder


def model_predict(body: Request, xgboost_model):
    data = body.input_data

    # pre process data
    df_predict = pre_process_input(data)

    # predict using trained model
    df_predictions = xgboost_model.predict(df_predict)

    return jsonable_encoder(df_predictions.to_dict('records'))
