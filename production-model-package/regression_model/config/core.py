# import the libraries
from pathlib import Path
from typing import Dict, List, Sequence
from pydantic import BaseModel  # Data validation and settings management using Python type hinting.
from strictyaml import load, \
    YAML  # StrictYAML is a type-safe YAML parser that parses and validates a restricted subset of the YAML specification.
import regression_model

# Project directories
PACKAGE_ROOT = Path(regression_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODELS_DIR = PACKAGE_ROOT / "trained_models"
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"


# app level config validations

class AppConfig(BaseModel):
    """
    Application level config.
    """
    package_name: str
    training_data_file: str
    testing_data_file: str
    pipeline_save_file: str


class ModelConfig(BaseModel):
    """
    All configurations relevant to model and features
    """
    target: str
    features: List[str]
    test_size: float
    random_state: int
    ##


class Configs(BaseModel):
    """Master config object"""
    app_configs: AppConfig
    model_configs: ModelConfig


# get config file path
def get_config_file() -> Path:
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config file not found at {CONFIG_FILE_PATH!r}")


def get_config_from_yaml(cfg_path: Path = None) -> YAML:
    if not cfg_path:
        cfg_path = get_config_file()
    if cfg_path:
        with open(cfg_path, "r") as cfg_file:
            parsed_conf = load(cfg_file.read())
            return parsed_conf
    raise OSError(f"Did not find config file at path :{cfg_path}")


#
def create_and_validate_config(parsed_conf: YAML = None) -> Configs:
    if parsed_conf is None:
        parsed_conf = get_config_from_yaml()

    _configs = Configs(app_configs=AppConfig(**parsed_conf.data),
                       model_configs=ModelConfig(**parsed_conf.data))

    return _configs


configs = create_and_validate_config()
