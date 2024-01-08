from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
from src.red_wine_project.utils.common import create_directories
import os,sys 
import zipfile
import urllib.request as request
from src.red_wine_project.entity.config_entity import DataIngestionConfig
from src.red_wine_project.entity.artifact_entity import DataIngestionArtifact
import pandas as pd 
from sklearn.model_selection import train_test_split

class DataIngestion:
    def __init__(self):
        try:
            self.data_ingestion_config=DataIngestionConfig()
            create_directories([self.data_ingestion_config.root_dir])
        except Exception as e:
            logging.info(f"{CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def download_file(self):
        try:
            logging.info(f"downloading data for data ingestion stage")
            os.makedirs(self.data_ingestion_config.raw_data_dir,exist_ok=True)
            if not os.path.exists(self.data_ingestion_config.raw_data_path):
                filename,headers=request.urlretrieve(
                    url=self.data_ingestion_config.dataset_download_URL,
                    filename=self.data_ingestion_config.raw_data_path
                )
                logging.info(f"{filename} downloaded with following info : \n{headers}")
            else:
                logging.info(f"file already exists of size ")
        except Exception as e:
            logging.info(f"data downloading interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
            
    def extract_zip_file(self):
        try:
            unzip_path=self.data_ingestion_config.extracted_data_dir
            os.makedirs(unzip_path,exist_ok=True)
            with zipfile.ZipFile(self.data_ingestion_config.raw_data_path,'r') as zip_reference:
                zip_reference.extractall(unzip_path)
            logging.info(f"unzipped downloaded dataset and store inside path : {unzip_path}")
        except Exception as e:
            logging.info(f"data extraction interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def split_dataset(self):
        try:
            logging.info(f"splitting extrated dataset into train and test dataset ")
            dataset_path=self.data_ingestion_config.ingested_dataset_dir
            os.makedirs(dataset_path,exist_ok=True)
            dataframe=pd.read_csv(self.data_ingestion_config.extracted_data_path)
            traindf,testdf=train_test_split(dataframe,test_size=0.2,random_state=44)
            logging.info(f"train data shape : {traindf.shape}, test data shape : {testdf.shape}")
            
            traindf.to_csv(self.data_ingestion_config.ingested_train_data_path)
            testdf.to_csv(self.data_ingestion_config.ingested_test_data_path)
            
            logging.info(f"training and testing dataset saved into path {self.data_ingestion_config.ingested_dataset_dir}")
            
        except Exception as e:
            logging.info(f"data splitting interrupted due to : {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            self.download_file()
            self.extract_zip_file()
            self.split_dataset()
            data_ingestion_artifact=DataIngestionArtifact(
                ingested_train_filepath=self.data_ingestion_config.ingested_train_data_path,
                ingested_test_filepath=self.data_ingestion_config.ingested_test_data_path,
                extracted_data_filepath=self.data_ingestion_config.extracted_data_path
                )
            logging.info(f"data ingestion artifact \n {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            logging.info(CustomException(e,sys))
            raise CustomException(e,sys)
        
    
            
    