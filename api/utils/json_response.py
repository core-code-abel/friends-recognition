from flask import Response
import pandas as pd

def process_col(col):
    return col.split('.')[-1].split(' AS ')[-1]

def json_response(data, cols):
    res = pd.DataFrame(data)
    res.columns = [process_col(col) for col in cols]
    return res.to_json(orient="records")
