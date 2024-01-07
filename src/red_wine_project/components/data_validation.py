from src.red_wine_project.entity.config_entity import DataValidationConfig
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
import os,sys 
import pandas as pd 
from src.red_wine_project.utils.common import read_yaml

class Datavalidation:
    def __init__(self,data_validation_config:DataValidationConfig):
        try:
            self.data_validation_config=data_validation_config
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    def validate_all_columns(self)-> bool:
        try:
            validation_status=None 
            data=pd.read_csv(self.data_validation_config.raw_data_dir)
            all_cols=list(data.columns)
            
            all_schema= self.data_validation_config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False 
                    with open(self.data_validation_config.status_file,'w') as file:
                        file.write(f"validation status : {validation_status}")
                else:
                    validation_status=True 
                    with open(self.data_validation_config.status_file,'w') as file:
                        file.write(f"validation status : {validation_status}")
            
            return validation_status
        
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    def initiate_data_validation(self):
        try:
            self.validate_all_columns()
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        