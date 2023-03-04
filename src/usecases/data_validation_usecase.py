import pandas as pd
import tensorflow_data_validation as tfdv

from src.utils.logging_utils import logger


def validate_data(df: pd.DataFrame, schema):

    serve_stats = tfdv.generate_statistics_from_dataframe(df)
    anomalies = tfdv.validate_statistics(serve_stats, schema, environment='SERVING')

    if anomalies.anomaly_info:
        logger().warning("Anomalies Detected in data")
        logger().warning(tfdv.display_anomalies(anomalies))
