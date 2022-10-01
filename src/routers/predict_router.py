from fastapi import APIRouter
from configs.routes import PREDICTION_ROUTE

router = APIRouter()


@router.post(PREDICTION_ROUTE)
def predict():
    pass
