import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
           preprocessor_path=os.path.join('artifacts','preprocessor.pkl') #code run in both linux and windows
           model_path=os.path.join('artifacts','model.pkl')

           preprocessor=load_object(preprocessor_path)
           model=load_object(model_path)

           data_scaled=preprocessor.transform(features)

           pred=model.predict(data_scaled)
           return pred
        
        
        
        
        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)  # type: ignore
        
class CustomData:
    def __init__(self,
                 Age:int,
                 Sex:str,
                 Sick:bool,
                 Pregnant:bool,
                 ThyroidSurgery:bool,
                 Goitre:bool,
                 Tumor:bool,
                 TSH:float,
                 T3:float,
                 TT4:float,
                 T4U:float,
                 FTI:float):
    
        self.Age=Age
        self.Sex=Sex
        self.Sick=Sick
        self.Pregnant=Pregnant
        self.ThyroidSurgery=ThyroidSurgery
        self.Goitre=Goitre
        self.Tumor=Tumor
        self.TSH=TSH
        self.T3=T3
        self.TT4=TT4
        self.T4U=T4U
        self.FTI=FTI
    
    
    
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'Age':[self.Age],
                'Sex':[self.Sex],
                'Sick':[self.Sick],
                'Pregnant':[self.Pregnant],
                'Thyroid Surgery':[self.ThyroidSurgery],
                'Goitre':[self.Goitre],
                'Tumor':[self.Tumor],
                'TSH':[self.TSH],
                'T3':[self.T3],
                'TT4':[self.TT4],
                'T4U':[self.T4U],
                'FTI':[self.FTI]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)  # type: ignore

