import os
import sys
import pandas as pd
import numpy as np

from src.utils.utils import load_model
from src.exception import CustomException
from src.logging  import logging


class PredictionPipeline():
    def __init__(self) -> None:
        pass

    def get_predict(self,feature):
        try:
            preprocessor_object = os.path.join('artifact','preprocessor.pkl')
            model_object  = os.path.join('artifact','model.pkl')
            preprocessor_model  = load_model(preprocessor_object)
            prediction_model  = load_model(model_object)
            
            scaled_features = preprocessor_model.transform(feature)
            value = prediction_model.predict(scaled_features)
            return value  
        except Exception as e:
            raise CustomException(e,sys)
        





class CustomEntry():
    def __init__(self,carat ,cut,color,clarity, depth, table, x, y,z) -> None:
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth  = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z

    def get_data_frame(self):
        df_dict  ={'carat':[self.carat],
                   'cut':[self.cut],
                   "color":[self.color],
                   "clarity":[self.clarity],
                   "depth":[self.depth],
                   "table":[self.table],  
                   "x":[self.x],
                   "y":[self.y],
                   "z":[self.z]}
        return pd.DataFrame(df_dict)
    



# obj = PredictionPipeline()
# column_names = ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']
# feature = np.array([[0.59, 'Ideal', 'E', 'VS2', 62.1, 55.0, 5.40, 5.42, 3.36]])

# feature = pd.DataFrame(feature,columns=column_names)
# print(feature)
# obj.get_predict(feature)



# input_obj = CustomEntry(0.59,  'Ideal' ,'E','VS2',62.1,55.0,5.4,5.42,3.36)
# df = input_obj.get_data_frame()
# print(df)