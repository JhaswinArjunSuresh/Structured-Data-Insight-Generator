import pandas as pd
import io

def profile_csv(file_bytes):
    df = pd.read_csv(io.BytesIO(file_bytes))
    profile = {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing": df.isnull().sum().to_dict(),
    }
    numeric_cols = df.select_dtypes(include='number')
    if not numeric_cols.empty:
        desc = numeric_cols.describe().to_dict()
        profile["statistics"] = desc
    return profile

