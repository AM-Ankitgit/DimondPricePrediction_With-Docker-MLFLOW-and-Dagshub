from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


data = DataIngestion()
path1,path2  =data.initiate_data_ingestion()
obj_data_trans = DataTransformation()
arr1,arr2 = obj_data_trans.initialize_data_transformation(path1,path2)

model_trainer = ModelTrainer()
model_trainer.initate_model_training(arr1,arr2)