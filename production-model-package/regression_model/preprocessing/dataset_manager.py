from pathlib import Path
import pandas as pd
import joblib
from regression_model.config.core import DATASET_DIR, TRAINED_MODELS_DIR
from sklearn.pipeline import Pipeline
from regression_model.config.core import configs
import regression_model.__version__ as _version


# function to load the data
def load_dataset(*, filename: str) -> pd.DataFrame:
    data = pd.read_csv(Path(f"{DATASET_DIR}/{filename}"))
    return data


def save_pipeline(*, pipeline_to_persist: Pipeline) -> None:
    save_file_name = f"{configs.app_configs.pipeline_save_file}/{_version}.pkl"
    save_file_path = TRAINED_MODELS_DIR / save_file_name
    joblib.dump(pipeline_to_persist, save_file_path)


def load_pipeline(*, filename: str) -> Pipeline:
    pipeline_path = TRAINED_MODELS_DIR / filename
    trained_model = joblib.load(filename=pipeline_path)
    return trained_model
