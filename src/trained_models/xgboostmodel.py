import os

import pandas as pd
import xgboost as xgb

from configs.constants import MODEL_PATH, XGBOOST_MODEL_NAME, PREDICTION_THRESHOLD, RETURN_FEATURE_NAME
from src.utils.logging_utils import logger


class XGBoostModel:

    def __init__(self):
        self.model = xgb.Booster()
        logger().info('Loading Model')
        self.model.load_model(os.path.join(MODEL_PATH, XGBOOST_MODEL_NAME))
        logger().info('Model Loaded')

    def predict(self, data: pd.DataFrame) -> pd.DataFrame:

        dPred = xgb.DMatrix(data)
        predictions = list(self.model.predict(dPred) > PREDICTION_THRESHOLD)

        df_pred = pd.DataFrame()
        df_pred[RETURN_FEATURE_NAME] = predictions

        return df_pred
