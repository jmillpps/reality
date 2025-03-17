import pytest
import os
import sys

# Set PYTHONPATH to src/
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

if __name__ == "__main__":
    print("Running all tests in the tests/ directory...\n")
    pytest.main(["-v", "tests/"])
