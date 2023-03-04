XGBOOST_MODEL_NAME = 'xgboost_bst.ubj'
MODEL_PATH = 'src/data/model/'
SCHEMA_FILE_PATH = 'src/data/schema/schema.pbtxt'

PREDICTION_THRESHOLD = 0.5
RETURN_FEATURE_NAME = 'is_attributed'

DTYPES = {
    'ip': 'uint32',
    'app': 'uint16',
    'device': 'uint16',
    'os': 'uint16',
    'channel': 'uint16',
    'click_time': 'datetime',
    'attributed_time': 'str'
}
