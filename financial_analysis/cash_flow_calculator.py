import pandas as pd

def calculate_free_cash_flow(df):
    """
    Calculates Free Cash Flow for a given DataFrame.
    Formula: Free Cash Flow = Operating Cash Flow - Capital Expenditures
    """
    # Create a copy so we don't accidentally modify the original data
    result_df = df.copy()
    
    # Calculate the new column
    result_df['Free Cash Flow'] = result_df['Operating Cash Flow'] - result_df['Capital Expenditures']
    
    return result_df

def calculate_operating_cash_flow_ratio(df):
    """
    Calculates Operating Cash Flow Ratio.
    Formula: Operating Cash Flow / Current Liabilities
    """
    result_df = df.copy()
    
    # We add a small number (0.0001) to avoid dividing by zero if liabilities are 0
    result_df['Operating Cash Flow Ratio'] = result_df['Operating Cash Flow'] / (result_df['Current Liabilities'] + 0.0001)
    
    return result_df

def run_all_cash_flow_calculations(df):
    """
    A helper function to run all cash flow calculations at once.
    """
    df = calculate_free_cash_flow(df)
    df = calculate_operating_cash_flow_ratio(df)
    return df
