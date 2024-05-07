from dataclasses import dataclass
from pathlib import Path

from flask.testing import FlaskClient

# Defining the object of data that will be ingested/used for the project  
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataPreProcessingConfig:
    resize_width: int
    resize_height: int

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str

