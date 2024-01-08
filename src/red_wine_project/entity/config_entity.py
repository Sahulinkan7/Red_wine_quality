from dataclasses import dataclass
from pathlib import Path
import os 
from src.red_wine_project.utils.common import read_yaml


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : str = os.path.join("artifacts","data_ingestion")
    dataset_download_URL: str = str("https://github.com/Sahulinkan7/dataset_repo/raw/main/winequality-red.zip")
    raw_data_dir: str = os.path.join(root_dir,"raw_data")
    raw_data_path: str = os.path.join(raw_data_dir,"data.zip")
    extracted_data_dir : str = os.path.join(root_dir,"extracted_data")
    extracted_data_path: str = os.path.join(extracted_data_dir,"winequality-red.csv")
    ingested_dataset_dir: str = os.path.join(root_dir,"ingested_dataset")
    ingested_train_data_path : str = os.path.join(ingested_dataset_dir,"train.csv")
    ingested_test_data_path : str = os.path.join(ingested_dataset_dir,"test.csv")
    
 
@dataclass 
class DataValidationConfig:
    root_dir: Path = os.path.join("artifacts","data_validation")
    status_file: str = os.path.join(root_dir,"validation_status.txt")
    schema_file_path: str = os.path.join("schema.yaml")
    
@dataclass
class DataTransformationConfig:
    root_dir: Path = os.path.join("artifacts","data_transformation")
    transformed_data_dir = os.path.join(root_dir,"transformed")
    transformed_train_file_path: str = os.path.join(transformed_data_dir,"train.npy")
    transformed_test_file_path: str = os.path.join(transformed_data_dir,"test.npy")
    transformed_object_dir: str = os.path.join(root_dir,"transformed_object")
    transformed_object_filepath : str = os.path.join(transformed_object_dir,"preprocessor.pkl")