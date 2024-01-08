from  dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    ingested_train_filepath: str
    ingested_test_filepath: str
    extracted_data_filepath: str
    

@dataclass
class DataValidationArtifact:
    validation_status: bool
    validated_data: str
    validated_train_data_filepath: str
    validated_test_data_filepath: str
    
@dataclass
class DataTransformationArtifact:
    transformed_train_file_path : str
    transformed_test_file_path : str
    transformed_object_file_path : str
    
