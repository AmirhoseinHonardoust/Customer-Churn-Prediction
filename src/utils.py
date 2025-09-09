import pandas as pd
from sklearn.model_selection import train_test_split

def load_dataset(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def split_xy(df: pd.DataFrame, test_size: float, val_size: float, seed: int):
    X = df.drop(columns=["churn", "customer_id"])
    y = df["churn"].astype(int)
    X_tmp, X_test, y_tmp, y_test = train_test_split(X, y, test_size=test_size, stratify=y, random_state=seed)
    X_train, X_val, y_train, y_val = train_test_split(X_tmp, y_tmp, test_size=val_size, stratify=y_tmp, random_state=seed)
    return X_train, X_val, X_test, y_train, y_val, y_test
