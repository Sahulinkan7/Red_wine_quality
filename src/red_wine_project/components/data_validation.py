from src.red_wine_project.entity.config_entity import DataValidationConfig
from src.red_wine_project.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
import os,sys 
import pandas as pd 
from src.red_wine_project.utils.common import create_directories
from src.red_wine_project.utils.common import read_yaml

class Datavalidation:
    def __init__(self,data_ingestion_artifact : DataIngestionArtifact):
        try:
            self.data_validation_config=DataValidationConfig()
            self.data_ingestion_artifact= data_ingestion_artifact
            create_directories([self.data_validation_config.root_dir])
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    def validate_all_columns(self,data_file_path)-> bool:
        try:
            logging.info(f"validating all columns inside dataframe")
            validation_status=None 
            data=pd.read_csv(data_file_path)
            all_cols=list(data.columns)
            logging.info(f"reading all columns present inside dataframe \n {all_cols}")
            schema=read_yaml(self.data_validation_config.schema_file_path)
            all_schema= schema['COLUMNS'].keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False 
                    with open(self.data_validation_config.status_file,'w') as file:
                        file.write(f"validation status : {validation_status}")
                else:
                    validation_status=True 
                    with open(self.data_validation_config.status_file,'w') as file:
                        file.write(f"validation status : {validation_status}")
            logging.info(f"validation status is {validation_status}")
            return validation_status
        
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            
            validated_data=self.data_ingestion_artifact.extracted_data_filepath
            status=self.validate_all_columns(data_file_path=validated_data)
            data_validation_artifact=DataValidationArtifact(validation_status=status,
                                                            validated_data=validated_data,
                                                            validated_train_data_filepath=self.data_ingestion_artifact.ingested_train_filepath,
                                                            validated_test_data_filepath=self.data_ingestion_artifact.ingested_test_filepath)
            return data_validation_artifact
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        