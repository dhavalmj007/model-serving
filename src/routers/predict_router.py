from fastapi import APIRouter
from configs.routes import PREDICTION_ROUTE
from src.models.router_models import Request, ReturnModel
from src.usecases.predict_usecase import model_predict
from src.trained_models.xgboost_model import XGBoost_Model

router = APIRouter()

# initilize the model
xgboost_model = XGBoost_Model()


@router.post(PREDICTION_ROUTE)
def predict(body: Request) -> ReturnModel:
    """"
    Simple XGBoost model prediction API
    :param body: input features

    :return: predictions
    """
    prediction = model_predict(body, xgboost_model)

    return prediction
