from typing import Any
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvalution
from src.logging import logging
from src.exception import CustomException
import sys

class TrainingPipeline():
    def __init__(self) -> None:
        pass

    def start_data_ingestion(self):
        try:
            data = DataIngestion()
            train_path,test_path  =data.initiate_data_ingestion()
            return (train_path,test_path)
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_data_transformation(self,train_path,test_path):
        try:
            obj_data_trans = DataTransformation()
            training_arr,testing_arr= obj_data_trans.initialize_data_transformation(train_path,test_path)
            return training_arr,testing_arr
        except Exception as e:
            raise CustomException( e,sys)
        


    def start_model_training(self,training_arr,testing_arr):
        try:

            model_trainer = ModelTrainer()
            model_trainer.initate_model_training(training_arr,testing_arr)

            # obj = ModelEvalution()
            # obj.initiate_model_eval(training_arr,testing_arr)
        except Exception as e:
            raise CustomException(e,sys)
    
    def start_training(self):
        train_path,test_path = self.start_data_ingestion()
        training_arr,testing_arr = self.start_data_transformation(train_path,test_path)
        self.start_model_training(training_arr,testing_arr)
        
        

# training_obj = TrainingPipeline()
# training_obj.start_training()