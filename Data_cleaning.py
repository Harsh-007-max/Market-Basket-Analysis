#!/usr/bin/env python3
import pandas as pd


def cleanData(tableName="groceries - groceries.csv",columnsToDrop=['Item(s)']):
    # importing the dataset which is going to be cleaned
    # dataset = pd.read_csv('groceries - groceries.csv')
    dataset = pd.read_csv(tableName)
    
    # removing index column
    dataset_without_items = dataset.drop(columns=columnsToDrop)
    
    # getting unique values from the dataset to create columns in the output dataset
    unique_values = dataset_without_items.stack().unique()
    
    # creating the output dataset with columns as unique values and rows as the transactions & filling it with 0 & 1 respectively
    output_dataset = pd.DataFrame(0, index=range(len(dataset)), columns=unique_values)
    for i,value in dataset_without_items.iterrows():
        for item in value:
            if item in output_dataset.columns:
                output_dataset.at[i, item] = 1
    
    # writing the output dataset to a file groceries_cleaned.csv which contains the cleaned dataset
    # output_dataset.to_csv('groceries_cleaned.csv', index=False)
    tableName = tableName.split(".")[0]
    output_dataset.to_csv(tableName+'_cleaned.csv', index=False)
    print(f"Cleanded data {tableName+"_cleaned.csv"}")
    return tableName+'_cleaned.csv'
