from pathlib import Path
from src.red_wine_project.exception import CustomException
from src.red_wine_project.logger import logging
import yaml,sys,os

def read_yaml(path_to_yaml:Path)->dict:
    try:
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