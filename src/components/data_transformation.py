from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler

from src.utils.utils import save_object

import pandas as pd
import numpy as np
from src.logging import logging
from src.exception import CustomException
import os
import sys
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifact','preprocessor.pkl')


class DataTransformation:



    def  __init__(self) -> None:
        self.data_transformation_config = DataTransformationConfig


    
    def get_data_transformation(self):
        logging.info("data transformation initiated")
        try:
            # Define which columns should be ordinal-encoded and which should be scaled
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            
            # Define the custom ranking for each ordinal variable
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info('Pipeline Initiated')



            ## transform the numerical columns : Numerical Pipeline
            num_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ])
            
            ## ## transform the Categorical columns : Categorical Pipeline
            cat_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoding',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ])
            
            # compose the numerical and the categorical pipeline

            #Note when we pass the data to preprocessor of ColumnsTransforme need to in dataframe (in predicion also)
            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols),

            ])

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    

    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(train_path)
            print(test_df.head(2))

            logging.info("reading train and test completed")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')

            processed_object = self.get_data_transformation()

            target_col_name = 'price'
            input_feature_train_df = train_df.drop([target_col_name],axis=1)
            target_feature_train_df = train_df[target_col_name].values

            input_feature_test_df = test_df.drop([target_col_name],axis=1)
            target_feature_test_df = test_df[target_col_name]

            train_transform = processed_object.fit_transform(input_feature_train_df)
            test_transform  = processed_object.transform(input_feature_test_df)

            # convert the train and test in array with target variable

            # concatenate 2d array with one more columns
            train_arr = np.c_[train_transform,target_feature_train_df]
            test_arr = np.c_[test_transform,target_feature_test_df]

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        model=processed_object)
            logging.info('preproessing object save in artifact folder')

            return (
                train_arr,test_arr
            )
            
        except Exception as e:
            raise CustomException(e,sys)