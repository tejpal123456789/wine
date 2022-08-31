# get params
# process the data
# return dataframe
import os
import pandas as pd
import yaml
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config    
def get_data(config_path):
    data=read_params(config_path)
    data_path=data['data_source']['s3_source']
    df=pd.read_csv(data_path,sep=',',encoding='utf8')
    
    return df

    
if __name__=='__main__':

    args=argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')

    parse_arg=args.parse_args()
    get_data(config_path=parse_arg.config)



