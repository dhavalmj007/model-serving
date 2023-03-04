from fastapi import APIRouter

from configs.constants import SCHEMA_FILE_PATH
from configs.routes import PREDICTION_ROUTE
from src.models.router_models import Request, ReturnModel
from src.usecases.predict_usecase import model_predict
from src.trained_models.xgboost_model import XGBoost_Model
import tensorflow_data_validation as tfdv

router = APIRouter()

# initialize the model and schema
xgboost_model = XGBoost_Model()
schema = tfdv.load_schema_text(SCHEMA_FILE_PATH)


@router.post(PREDICTION_ROUTE)
def predict(body: Request) -> ReturnModel:
    """
    Simple XGBoost model prediction API
    :param body: input features

    :return: predictions
    """
    prediction = model_predict(body, xgboost_model, schema)

    return prediction
