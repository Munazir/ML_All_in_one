# import the libraries
from pathlib import Path
from typing import Dict, List, Sequence
from pydantic import BaseModel
from strictyaml import load , YAML  # StrictYAML is a type-safe YAML parser that parses and validates a restricted subset of the YAML specification.
import regression_model

# Project directories
PACKAGE_ROOT = Path(regression_model.__file__).resolve().parent

