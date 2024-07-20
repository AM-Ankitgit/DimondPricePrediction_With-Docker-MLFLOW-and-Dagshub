from src.exception import CustomException
from src.logging import logging

import pandas as pd
import numpy as np
import os
import sys


from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path:str   = os.path.join("artifact","raw.csv")
    train_data_path:str = os.path.join("artifact","train.csv")
    test_data_path:str = os.path.join("artifact","test.csv")



class DataIngestion:
    def __init__(self) -> None:
        self.data_ingestion = DataIngestionConfig
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        try:
            data = pd.read_csv("data/raw.csv",)
            data = data.drop('Unnamed: 0',axis=1)

            logging.info('reading raw data')

            os.makedirs(os.path.dirname(os.path.join(self.data_ingestion.raw_data_path)),exist_ok=True)
            data.to_csv(self.data_ingestion.raw_data_path,index=False)
            logging.info("raw data stored in  the artifact")

            from sklearn.model_selection import train_test_split
            train,test = train_test_split(data,test_size=0.25)
            logging.info("train test perform")

            train.to_csv(self.data_ingestion.train_data_path,index=False)
            test.to_csv(self.data_ingestion.test_data_path)
            logging.info("train test data store in the artifact")


            # return  the path train test folder
            return (self.data_ingestion.train_data_path,
                    self.data_ingestion.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)
    


