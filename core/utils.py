import pandas as pd
import numpy as np

def format_currency(value):
    """
    Formats a number as currency (e.g., $1,000.00).
    This is a helper function to make our dashboard look nicer.
    """
    return f"${value:,.2f}"

def generate_mock_financial_data(num_companies=5):
    """
    Generates fake financial data so we can test our calculations and dashboard
    without needing real data right away.
    
    Returns a pandas DataFrame (which is like a table or spreadsheet in Python).
    """
    # Create an empty list to store our fake company data
    data = []
    
    # Generate data for a few fake companies
    for i in range(1, num_companies + 1):
        # We use random numbers to make the data look somewhat realistic
        revenue = np.random.uniform(500000, 2000000)
        cogs = revenue * np.random.uniform(0.4, 0.7) # Cost of Goods Sold is a percentage of revenue
        operating_expenses = revenue * np.random.uniform(0.1, 0.2)
        
        # Calculate some basic profits
        gross_profit = revenue - cogs
        operating_profit = gross_profit - operating_expenses
        net_income = operating_profit * 0.8 # Assume 20% tax roughly
        
        # Cash flow items
        operating_cash_flow = net_income + np.random.uniform(10000, 50000) # Add back depreciation
        capital_expenditures = np.random.uniform(20000, 100000)
        
        # Balance sheet items
        current_assets = np.random.uniform(200000, 500000)
        inventory = current_assets * np.random.uniform(0.2, 0.5)
        current_liabilities = np.random.uniform(100000, 300000)
        
        # New additions for EBIT and Equity ratio
        ebit = operating_profit  # In our simple model, EBIT is Operating Profit
        total_assets = current_assets + np.random.uniform(300000, 800000)
        total_equity = np.random.uniform(200000, 600000)
        
        # Append this company's data to our list as a dictionary
        data.append({
            "Company": f"Company {chr(64+i)}", # Company A, Company B, etc.
            "Revenue": revenue,
            "Cost of Goods Sold": cogs,
            "Operating Expenses": operating_expenses,
            "Gross Profit": gross_profit,
            "Operating Profit": operating_profit,
            "EBIT": ebit,
            "Net Income": net_income,
            "Operating Cash Flow": operating_cash_flow,
            "Capital Expenditures": capital_expenditures,
            "Current Assets": current_assets,
            "Total Assets": total_assets,
            "Inventory": inventory,
            "Current Liabilities": current_liabilities,
            "Total Equity": total_equity
        })
        
    # Convert the list of dictionaries into a pandas DataFrame (a table)
    df = pd.DataFrame(data)
    return df
