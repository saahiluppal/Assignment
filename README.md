# Interview Assignment - Decentral

### Problem Statement
Create unit-test to verify the overall schema and consistency of the input expected vs the input provided

```bash
# Input Schema
{"name": "sheet2","freeze": "A1","styles": [],"merges": [],"rows": {},"validations": []}
```

### Test Cases Covered in the code

#### Test Case 1
- Weather the provided input is actually in dictionary (HashMap) format or not
```
# Cases that will fail
input = "any string"          # because this is a string, not a dictionary
input = 8128                  # because this is an integer, not a dictionary
input = ['random', 'value']   # because this is a list, not a dictionary

# Cases that will pass
input = {"name": "sheet2","freeze": "A1","styles": [],"merges": [],"rows": {},"validations": []}
input = {}                        # This will pass, because this is a dictionary, further tests will reject if necessary elements are not present
input = {"element": "value"}      # same as before

```

#### Test Case 2
- Check weather all the required elements are present within the input dictionary
```
# Cases that will fail
# all the inputs, where required keys are not present, will FAIL
input = {}
input = {"element": "value", "another_element": "another_value"}

# Cases that will pass
# If the required keys are present, test case will pass, not matter what is the corresponding value; 
# Next test case will take care of values
input = {"name": "sheet2","freeze": "A1","styles": [],"merges": [],"rows": {},"validations": []}
input = {"name": "sheet2","freeze": 1000,"styles": {},"merges": {},"rows": {},"validations": []}
```

#### Test Case 3
- Check weather the assigned values to each element have correct datatype
```
# Cases that will fail
Corresponding values should match the data types present in input schema
input = {"name": "sheet2","freeze": 1000,"styles": {},"merges": {},"rows": {},"validations": []}
input = {"name": 43987349,"freeze": [],"styles": {},"merges": {},"rows": {},"validations": []}

# Cases that will pass
input = {"name": "sheet2","freeze": "A1","styles": [],"merges": [],"rows": {},"validations": []}
input = {"name": "","freeze": "","styles": [],"merges": [],"rows": {},"validations": []}
```

* By Applying these 3 test cases, we can make sure that the input provided must match the required schema.

### Code Execution
There are two files present in the folder structure. (README.md can be ignored)
```
├── data.txt
└── test_module.py
```
* Update the data.txt to simulate the input and then execute the `test_module.py` file.
* There are no dependencies; vanilla installation of python will be enough.

```bash
$ python test_module.py
```

### Additional Information
* This code is written in Python instead of JavaScript; Because i have a very little knowledge of how javascript works.
* Code is highly commented.
