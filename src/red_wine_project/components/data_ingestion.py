
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
import os,sys 
import zipfile
import urllib.request as request
from src.red_wine_project.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            logging.info(f"{CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_file(self):
        try:
            if not os.path.exists(self.data_ingestion_config.local_data_file):
                filename,headers=request.urlretrieve(
                    url=self.data_ingestion_config.dataset_download_URL,
                    filename=self.data_ingestion_config.local_data_file
                )
                logging.info(f"{filename} downloaded with following info : \n{headers}")
            else:
                logging.info(f"file already exists of size ")
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
            
    def extract_zip_file(self):
        try:
            unzip_path=self.data_ingestion_config.raw_data_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.data_ingestion_config.local_data_file,'r') as zip_reference:
                zip_reference.extractall(unzip_path)
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            self.download_file()
            self.extract_zip_file()
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    
            
    