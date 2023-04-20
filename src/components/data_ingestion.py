# data_ingestion is reading the dataset, path to save perticler format and create the train and test dataset
import os # to create path, join path
import sys # system error
from src.logger import logging # logger
from src.exception import CustomException #
import pandas as pd # read the dataset
from sklearn.model_selection import train_test_split # split the dataset
from dataclasses import dataclass # we can create directly variable vthout using init

from src.components.data_transformation import DataTransformation
'''use above src.components for train_data_path and test_data_path
#we use it for data_transformation.py
'''


## Intitialize the Data Ingetion Configuration

@dataclass # create constructor
class DataIngestionconfig: # here we no need to give init function ,bcoz we use dataclass
    train_data_path:str=os.path.join('artifacts','train.csv') # creating folders vth artifacts as train.csv,etc
    #train_data_path:str means path is string formart,artifacts is a folder name
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## create a class for Data Ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig() # calling dataingetionconfig 

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion methods Starts')
        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            #df=pd.read_csv('notebooks/data/gemstone.csv') #we can read datset like this also
            logging.info('Dataset read as pandas Dataframe')

            #make dir name
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)#  exist_ok=true is used for already exits path, it wotnt create 
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
  
            
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)
        
# run the data ingestion # video time:1:00
#it will create artfacts folder vth test,train,raw.csv files
'''
if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()       


# for data_transformation we use it ,after write code in it
'''  
# preprocessor.pkl file will created under artifact if u run this
if __name__=='__main__':
        obj=DataIngestion()  
        train_data_path,test_data_path=obj.initiate_data_ingestion()       
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data_path, test_data_path)
        # to execute this enable src.components import funtcion
        # we can use this code in training_pipeline under pipeline folder
        