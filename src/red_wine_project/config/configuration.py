from src.red_wine_project.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH,SCHEMA_FILE_PATH
from src.red_wine_project.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
import os,sys 
from src.red_wine_project.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.schema=read_yaml(schema_filepath)
        create_directories([self.config['artifacts_root']])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion_config=self.config['data_ingestion']
        
        create_directories([data_ingestion_config['root_dir']])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=data_ingestion_config['root_dir'],
            dataset_download_URL=data_ingestion_config['dataset_download_URL'],
            local_data_file=data_ingestion_config['local_data_file'],
            raw_data_dir=data_ingestion_config['raw_data_dir']
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self)->DataValidationConfig:
        data_validation_config= self.config['data_validation']
        schema= self.schema['COLUMNS']
        
        create_directories([data_validation_config['root_dir']])
        
        data_validation_config=DataValidationConfig(
            root_dir=data_validation_config['root_dir'],
            status_file=data_validation_config['STATUS_FILE'],
            raw_data_dir=data_validation_config['raw_data_dir'],
            all_schema=schema
        ) 

        return data_validation_config