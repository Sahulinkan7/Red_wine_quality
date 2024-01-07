from src.red_wine_project.components.data_ingestion import DataIngestion
from src.red_wine_project.components.data_validation import Datavalidation
from src.red_wine_project.config.configuration import ConfigurationManager

c=ConfigurationManager()

class TrainPipeline:
    is_running=False
    def __init__(self) -> None:
        self.configuration=ConfigurationManager()
    def start_data_ingestion(self):
        data_ingestion_config=self.configuration.get_data_ingestion_config()
        dataingestion_component=DataIngestion(data_ingestion_config=data_ingestion_config)
        dataingestion_component.initiate_data_ingestion()
        
    def start_data_validation(self):
        data_validation_config=self.configuration.get_data_validation_config()
        data_validation_component=Datavalidation(data_validation_config=data_validation_config)
        data_validation_component.initiate_data_validation()
            
    def start_data_transformation(self):
        pass
    
    def start_model_trainer(self):
        pass
    
    def start_model_evaluation(self):
        pass
        
    def start_training(self):
        TrainPipeline.is_running=True
        self.start_data_ingestion()
        self.start_data_validation()
        TrainPipeline.is_running=False