import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from utils import yaml_parser
from utils.data_types import Table

"""
test.yml contents:
tables:
  - name: securities
    description: Master list of all tradable securities and their attributes
    columns:
      - name: ticker
        description: Stock ticker symbol (e.g., AAPL, MSFT)
      - name: sector
        description: Industry sector classification
      - name: market_cap
        description: Market capitalization in USD

  - name: prices
    description: Historical OHLC price and volume data for securities
    columns:
      - name: date
        description: Trading date in YYYY-MM-DD format
      - name: open
        description: Opening price for the trading day
      - name: close
        description: Closing price for the trading day
      - name: volume
        description: Number of shares traded
"""
def test_parse_yaml_to_tables():
    with open(current_dir+"/test.yml") as f:
        yaml_content = f.read()
        tables = yaml_parser.parse_yaml_to_tables(yaml_content)
        assert len(tables) == 2
        assert isinstance(tables[0], Table)
        assert tables[0].name == "securities"
        assert tables[0].description == "Master list of all tradable securities and their attributes"
        assert len(tables[0].columns) == 3
        assert tables[0].columns[0].name == "ticker"
        assert tables[0].columns[0].description == "Stock ticker symbol (e.g., AAPL, MSFT)"
        assert tables[0].columns[1].name == "sector"
        assert tables[0].columns[1].description == "Industry sector classification"
        assert tables[0].columns[2].name == "market_cap"
        assert tables[0].columns[2].description == "Market capitalization in USD"
        assert isinstance(tables[1], Table)
        assert tables[1].name == "prices"
        assert tables[1].description == "Historical OHLC price and volume data for securities"
        assert len(tables[1].columns) == 4
        assert tables[1].columns[0].name == "date"
        assert tables[1].columns[0].description == "Trading date in YYYY-MM-DD format"
        assert tables[1].columns[1].name == "open"
        assert tables[1].columns[1].description == "Opening price for the trading day"
        assert tables[1].columns[2].name == "close"
        assert tables[1].columns[2].description == "Closing price for the trading day"
        assert tables[1].columns[3].name == "volume"
        assert tables[1].columns[3].description == "Number of shares traded"
        f.close()

if __name__ == "__main__":
    test_parse_yaml_to_tables()
    print("All tests passed!")
    