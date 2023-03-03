from typing import List

import pandas as pd
import numpy as np
import xgboost as xgb
import os

from configs.constants import MODEL_PATH, XGBOOST_MODEL_NAME, PREDICTION_THRESHOLD, RETURN_FEATURE_NAME


class XGBoost_Model:

    def __init__(self):
        self.model = xgb.Booster()
        self.model.load_model(os.path.join(MODEL_PATH, XGBOOST_MODEL_NAME))

    def predict(self, data: pd.DataFrame) -> pd.DataFrame:

        dPred = xgb.DMatrix(data)
        predictions = list(self.model.predict(dPred) > PREDICTION_THRESHOLD)

        df_pred = pd.DataFrame()
        df_pred[RETURN_FEATURE_NAME] = predictions

        return df_pred
