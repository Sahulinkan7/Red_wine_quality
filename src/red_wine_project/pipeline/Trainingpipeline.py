from src.red_wine_project.components.data_ingestion import DataIngestion
from src.red_wine_project.components.data_validation import Datavalidation
from src.red_wine_project.components.data_transformation import DataTransformation
import os,sys 
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging

class TrainPipeline:
    is_running=False
    def __init__(self) -> None:
        pass
    def start_data_ingestion(self):
        try:
            logging.info(f"\n{'<<'*20} Data Ingestion stage started {'>>'*20}")
            dataingestion_object=DataIngestion()
            data_ingestion_artifact=dataingestion_object.initiate_data_ingestion()
            logging.info(f"\n{'<<'*20} Data Ingestion stage completed {'>>'*20}")
            return data_ingestion_artifact
        except Exception as e:
            logging.info(f"Data Ingestion stage Interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact):
        try:
            logging.info(f"\n{'<<'*20} Data Validation stage started {'>>'*20}")
            data_validation_object=Datavalidation(data_ingestion_artifact)
            validation_artifact=data_validation_object.initiate_data_validation()
            logging.info(f"\n{'<<'*20} Data Validation stage completed {'>>'*20}")
            return validation_artifact
        except Exception as e:
            logging.info(f"Data validation stage Interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
            
    def start_data_transformation(self,data_validation_artifact):
        try:
            logging.info(f"\n{'<<'*20} Data Transformation stage started {'>>'*20}")
            data_transformation=DataTransformation(data_validation_artifact=data_validation_artifact)
            transformation_artifact=data_transformation.initiate_data_transformation()
            logging.info(f"\n{'<<'*20} Data Transformation stage ended {'>>'*20}")
        except Exception as e:
            logging.info(f"Data Transformation stage Interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
    
    def start_model_trainer(self):
        pass
    
    def start_model_evaluation(self):
        pass
        
    def start_training(self):
        try:
            TrainPipeline.is_running=True
            logging.info(f"\n{'*'*20} Training Pipeline Started {'*'*20}")
            ingestion_artifact=self.start_data_ingestion()
            validation_artifact=self.start_data_validation(data_ingestion_artifact=ingestion_artifact)
            transformation_artifact=self.start_data_transformation(data_validation_artifact=validation_artifact)
            TrainPipeline.is_running=False
            logging.info(f"\n{'*'*20} Training Pipeline Completed {'*'*20}")
        except Exception as e:
            logging.info(f"Training pipeline Interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
        