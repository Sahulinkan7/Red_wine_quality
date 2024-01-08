
from src.red_wine_project.entity.config_entity import DataTransformationConfig
from src.red_wine_project.entity.artifact_entity import DataValidationArtifact,DataTransformationArtifact
from src.red_wine_project.logger import logging
from src.red_wine_project.exception import CustomException
from src.red_wine_project.utils.common import read_yaml,create_directories,save_object,save_numpy_array_data
import os,sys 
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from src.red_wine_project.constants import SCHEMA_FILE_PATH
from imblearn.over_sampling import SMOTE
from imblearn.combine import SMOTETomek

class DataTransformation:
    def __init__(self,data_validation_artifact: DataValidationArtifact):
        self.data_transformation_config=DataTransformationConfig()
        self.data_validation_artifact=data_validation_artifact
        create_directories([self.data_transformation_config.root_dir])
    
    def get_data_transformer_object(self):
        try:
            logging.info(f"creating data transformer object ")
            
            logging.info("creating pipeline for data transformer object")
            preprocessor=Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
            ])
            logging.info("pipeline for data transformer created")
            
            logging.info("data transformer object created")
            return preprocessor
        
        except Exception as e:
            logging.info(f"data transformer object creation inturrupted due to {CustomException(e,sys)}")
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            logging.info(f" reading dataframe ")
            train_dataframe=pd.read_csv(self.data_validation_artifact.validated_train_data_filepath)
            test_dataframe=pd.read_csv(self.data_validation_artifact.validated_test_data_filepath)
            
            preprocessor=self.get_data_transformer_object()
            target_column=list(read_yaml(SCHEMA_FILE_PATH)['TARGET_COLUMN'].keys())[0]
            
            # training dataframe splitting             
            logging.info(f"dropping target columns from training dataframe ")
            input_feature_train_df=train_dataframe.drop(columns=target_column,axis=1)
            target_feature_train_df=train_dataframe[target_column]
            logging.info(f"target column {target_column} dropped from train dataframe")
            logging.info(f"input feature train dataframe and target feature train dataframe created successfully.")
            
            # test dataframe splitting             
            logging.info(f"dropping target columns from testing dataframe ")
            input_feature_test_df=test_dataframe.drop(columns=target_column,axis=1)
            target_feature_test_df=test_dataframe[target_column]
            logging.info(f"target column {target_column} dropped from test dataframe")
            logging.info(f"input feature test dataframe and target feature test dataframe created successfully.")
            
            logging.info(f"fitting input training dataframe with preprocessor pipeline object to create transformation object")
            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_train_feature= preprocessor_object.transform(input_feature_train_df)
            transformed_input_test_feature=preprocessor_object.transform(input_feature_test_df)
            
            logging.info("input features of train and test dataframe got transformed")
            
            smt=SMOTE(k_neighbors=2)
            logging.info("resampling train and test dataframe ")
            input_feature_train_final,target_feature_train_final=smt.fit_resample(transformed_input_train_feature,target_feature_train_df)
            input_feature_test_final,target_feature_test_final=smt.fit_resample(transformed_input_test_feature,target_feature_test_df)
            logging.info(f"\n{target_feature_train_final.value_counts()}, input_feature shape is {target_feature_train_final.shape}")
            logging.info(f"\n{target_feature_test_final.value_counts()}, input_feature shape is {target_feature_test_final.shape}")
            logging.info("concatinating the transformed input individual train and test array")
            
            train_arr= np.c_[input_feature_train_final,np.array(target_feature_train_final)]
            test_arr= np.c_[input_feature_test_final,np.array(target_feature_test_final)]

            save_numpy_array_data(file_path=self.data_transformation_config.transformed_train_file_path,array=train_arr)
            save_numpy_array_data(file_path=self.data_transformation_config.transformed_test_file_path,array=test_arr)
            
            save_object(file_path=self.data_transformation_config.transformed_object_filepath,obj=preprocessor_object)
            logging.info(f"Data transformation preprocessor object saved successfully !")
            
            data_transformation_artifact= DataTransformationArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformed_object_file_path=self.data_transformation_config.transformed_object_filepath
            )
            logging.info(f"data transformation artifact \n {data_transformation_artifact}")
            return data_transformation_artifact
        
        except Exception as e:
            logging.info(f"{CustomException(e,sys)}")
            raise CustomException(e,sys)
            