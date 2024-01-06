import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="[%(asctime)s] : %(message)s")

ml_project_name="red_wine_project"

list_of_files=[
    f"src/{ml_project_name}/__init__.py",
    f"src/{ml_project_name}/components/__init__.py",
    f"src/{ml_project_name}/utils/__init__.py",
    f"src/{ml_project_name}/utils/common.py",
    f"src/{ml_project_name}/config/__init__.py",
    f"src/{ml_project_name}/config/configuration.py",
    f"src/{ml_project_name}/pipeline/__init__.py",
    f"src/{ml_project_name}/entity/__init__.py",
    f"src/{ml_project_name}/entity/config_entity.py",
    f"src/{ml_project_name}/constants/__init__.py",
    f"config/config.yaml",
    "params.yaml",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for file in list_of_files:
    filepath=Path(file)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory : {filedir} for file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file : {filepath}")
    
    else:
        logging.info("filepath exists")