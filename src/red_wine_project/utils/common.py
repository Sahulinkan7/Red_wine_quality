from pathlib import Path
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
import yaml,sys,os
import pickle
import numpy as np 


def read_yaml(path_to_yaml:Path)->dict:
    try:
        logging.info(f"reading yaml file content from {path_to_yaml}")
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully ")
            return content
    except Exception as e:
        logging.info(f"{CustomException(e,sys)}")
        raise CustomException(e,sys)
    
def create_directories(path_to_directories: list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created directory at path :  {path}")
            
def save_object(file_path: str, obj: object) :
    try:
        logging.info(f"saving object at file path : {file_path}")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,'wb') as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        logging.info(f"saving object interrupted due to : {CustomException(e,sys)}")
        raise CustomException(e,sys)
    
def load_object(file_path) -> object:
    try:
        logging.info(f"loading object from file path : {file_path}")
        if not os.path.exists(file_path):
            raise Exception(f"file path {file_path} does not exists ")
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info(f"loading object interrupted due to : {CustomException(e,sys)}")
        raise CustomException(e,sys)
    
    
def save_numpy_array_data(file_path : str ,array: np.array):
    try:
        logging.info(f" saving numpy array data ")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file:
            np.save(file,array)
        logging.info(f" numpy array data saved at file path {file_path}")
    except Exception as e:
        logging.info(f"saving numpy array data interrupted due to : {CustomException(e,sys)}")
        raise CustomException(e,sys)