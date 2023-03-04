from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse
from io import StringIO

from configs.constants import SCHEMA_FILE_PATH, PREDICTION_FILE_OUT_PATH
from configs.routes import PREDICTION_ROUTE, PREDICTION_FILE_ROUTE
from src.models.router_models import Request, ReturnModel
from src.usecases.predict_usecase import model_predict, model_predict_on_file
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


@router.post(PREDICTION_FILE_ROUTE)
def predict_on_file(file: UploadFile = File(...)) -> StreamingResponse:
    prediction = model_predict_on_file(file, xgboost_model, schema)

    return StreamingResponse(
        iter([prediction.to_csv(index=False)]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=response.csv"}
    )


