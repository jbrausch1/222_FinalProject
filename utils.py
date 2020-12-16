import pandas as pd
import numpy as np
import datetime as dt

def remove_negatives(df, column):
    '''
    
    '''
    temp_ser = df[column].copy()

    for i in range(0, len(temp_ser)):
        curr_string = str(temp_ser[i])
        if '-' in curr_string:
            temp_ser[i] = np.NaN
    
    df[column] = temp_ser
    df.dropna(0,'any',inplace=True)
    
def clean_descriptions(df, column1, column2):
    '''
    
    '''
    temp_ser = df[column1].copy()
    temp_ser2 = df[column2].copy()

    for i in range(0, len(temp_ser)):
        curr_string = temp_ser[i]
        cat_string = temp_ser2[i]
        if 'AMZN' in curr_string or 'Amazon' in curr_string:
            temp_ser[i] = 'Amazon.com'
        elif 'TARGET' in curr_string:
            temp_ser[i] = 'Target'
        elif 'DOORDASH' in curr_string:
            temp_ser[i] = 'DoorDash'
        elif 'SUBWAY' in curr_string:
            temp_ser[i] = 'Subway'
        elif 'MICROSOFT' in curr_string:
            temp_ser[i] = 'Microsoft'
        elif 'SAFEWAY' in curr_string:
            temp_ser[i] = 'Safeway'
        elif 'MCDONALD' in curr_string:
            temp_ser[i] = 'McDonalds'
        elif 'RIOT' in curr_string:
            temp_ser[i] = 'Riot Games'
        elif 'STEAM' in curr_string:
            temp_ser[i] = 'Steam'
        elif 'NIKE' in curr_string:
            temp_ser[i] = 'Nike'
        elif 'SUBWAY' in curr_string:
            temp_ser[i] = 'Subway'
        elif 'VENDING' in curr_string:
            temp_ser[i] = 'Vending Machine'
        elif 'SUNDAE' in curr_string:
            temp_ser[i] = 'Sundae Ice Cream'
        elif 'CHIPOTLE' in curr_string:
            temp_ser[i] = 'Chipotle'
        elif 'PATAGONIA' in curr_string:
            temp_ser[i] = 'Patagonia'
        elif 'DUTCH' in curr_string:
            temp_ser[i] = 'Dutch Bros'
        elif 'QDOBA' in curr_string:
            temp_ser[i] = 'Qdoba'
        elif 'ZAG' in curr_string:
            temp_ser[i] = 'Gonzaga'
        elif 'CHEGG' in curr_string:
            temp_ser[i] = 'Chegg'
        elif 'ESMERALDA' in curr_string:
            temp_ser[i] = 'Esmeralda Golf Course'
        elif 'PAYPAL' in curr_string:
            temp_ser[i] = 'PayPal'
        
    df[column1] = temp_ser

def write_csv(fname, df):
    '''
    
    '''
    out_file = open(fname, "w")
    df.to_csv(fname)
    out_file.close()       