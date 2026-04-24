import sys
import os

# This helps Python find our 'core' folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.utils import generate_mock_financial_data

def load_financial_data():
    """
    Loads financial data for the platform.
    Currently, it uses fake data for beginner practice.
    In the future, we could change this to read from an Excel or CSV file.
    """
    print("Loading mock financial data...")
    data = generate_mock_financial_data(num_companies=5)
    
    # We could do some 'normalization' here, which means making sure
    # all column names are standard, removing empty rows, etc.
    # For now, our mock data is already clean!
    
    return data

# This block allows us to run this file directly to test it
if __name__ == "__main__":
    df = load_financial_data()
    print("\nHere is a preview of the loaded data:")
    print(df.head()) # Shows the first 5 rows
