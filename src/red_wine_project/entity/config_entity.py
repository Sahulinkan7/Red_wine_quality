from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    dataset_download_URL: str
    local_data_file: Path
    raw_data_dir: Path
 
@dataclass(frozen=True)   
class DataValidationConfig:
    root_dir: Path
    status_file: str
    raw_data_dir: Path 
    all_schema: dict 