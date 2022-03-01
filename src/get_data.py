## Read params file
## process it
## return dataframe
import os
import pandas as pd
import argparse
import yaml

# Read params file
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# get data
def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["S3-source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")

    return df

## Main entry point
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)


