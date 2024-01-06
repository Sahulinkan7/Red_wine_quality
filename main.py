from src.red_wine_project.logger import logging
from src.red_wine_project.exception import CustomException
import sys 

def hello():
    try:
        c=9/0
    except Exception as e:
        logging.info(CustomException(e,sys))
        
        
hello()