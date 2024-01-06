import logging 
from datetime import datetime
import os,sys 

file_name=f"log_{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)
log_filepath=os.path.join(log_dir,file_name)
log_str="[%(asctime)s]-%(name)s-%(levelname)s : %(message)s"
logging.basicConfig(filename=log_filepath,
                    level=logging.INFO,
                    format=log_str,
                    )

