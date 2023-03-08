from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse

from configs.routes import PREDICTION_ROUTE, PREDICTION_FILE_ROUTE
from src.models.router_models import Request, ReturnModel
from src.trained_models.xgboostmodel import XGBoostModel
from src.usecases.predict_usecase import model_predict, model_predict_on_file

router = APIRouter()

# initialize the model and schema
xgboost_model = XGBoostModel()


@router.post(PREDICTION_ROUTE)
def predict(body: Request) -> ReturnModel:
    """
    Simple XGBoost model prediction API
    :param body: input features

    :return: predictions
    """
    prediction = model_predict(body, xgboost_model)

    return prediction


@router.post(PREDICTION_FILE_ROUTE)
def predict_on_file(file: UploadFile = File(...)) -> StreamingResponse:
    prediction = model_predict_on_file(file, xgboost_model)

    return StreamingResponse(
        iter([prediction.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=response.csv"}
    )


