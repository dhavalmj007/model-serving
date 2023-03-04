import gc

from src.models.router_models import Request
from src.usecases.pre_process_usecase import pre_process_input
from src.usecases.data_validation_usecase import validate_data
from fastapi.encoders import jsonable_encoder


def model_predict(body: Request, xgboost_model, schema):
    data = body.input_data

    # pre process data
    df_predict = pre_process_input(data, schema)

    # predict using trained model
    df_predictions = xgboost_model.predict(df_predict)

    return jsonable_encoder(df_predictions.to_dict('records'))
