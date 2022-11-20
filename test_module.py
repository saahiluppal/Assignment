import unittest

# Dummy Model Inputs are defined in this file
# Update file to simulate model inputs
DATA_PATH = "data.txt"

# Global variable SCHEMA defines what are the expected keys
# along with their corresponding datatypes
SCHEMA = {
    "name": str,
    "freeze": str,
    "styles": list,
    "merges": list,
    "rows": dict,
    "validations": list
}

class TestModelInput(unittest.TestCase):

    # Initialize everything required for the test case
    # Similar as constructor
    def setUp(self):
        with open(DATA_PATH) as handle:
            data = handle.readlines()
            self.data = eval(data[0])

    # Clean up resources that this test required
    # Similar to destructor
    def tearDown(self):
        del self.data

    # Test 1:
    # Check the actual datatype of the object passed as input
    # Expected Datatype = dictionary (HashMap)
    def test_datatype(self):
        self.assertIsInstance(self.data, dict)

    # Test 2:
    # Check weather all the required keys (elements) present in the input dictionary
    # REFER: Global variable SCHEMA
    def test_key_presence(self):
        for key in SCHEMA.keys():
            self.assertIn(
                key, self.data)

    # Test 3:
    # Check weather all the values assigned to the keys have correct datatype
    # REFER: Global variable SCHEMA
    def test_value_datatype(self):
        for key, value in SCHEMA.items():
            self.assertIsInstance(
                self.data[key], value)


# Run Tests
if __name__ == '__main__':
    unittest.main()
