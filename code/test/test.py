import unittest
import pandas as pd
from ai_data_profiling import validate_transaction  # Assuming this function handles transaction validation

class TestDataProfiling(unittest.TestCase):
    def setUp(self):
        """Set up a sample dataset for testing."""
        self.sample_data = pd.DataFrame({
            "Customer_ID": [123456],
            "Account_Balance": [-100],  # Negative balance (invalid)
            "Transaction_Amount": [500],
            "Reported_Amount": [500],
            "Currency": ["USD"],
            "Country": ["USA"],
            "Transaction_Date": ["2025-04-01"],  # Future date (invalid)
            "Risk_Score": [50]
        })

    def test_validate_transaction(self):
        """Test validation logic on transactions."""
        result = validate_transaction(self.sample_data.iloc[0])  
        self.assertTrue(result["Account_Balance"] < 0, "Account balance should not be negative")
        self.assertTrue(result["Transaction_Date"] > "2024-12-31", "Transaction date should not be in the future")

if __name__ == "__main__":
    unittest.main()
