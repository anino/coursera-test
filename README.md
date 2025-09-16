# coursera-test
Coursera Test Repository

This repository demonstrates basic testing concepts and provides a simple test framework for educational purposes.

## Files

- `calculator.py` - A simple calculator class with basic arithmetic operations
- `test_calculator.py` - Comprehensive test suite for the calculator class
- `run_tests.py` - Custom test runner script with detailed output

## Running Tests

You can run the tests in several ways:

### Using the custom test runner:
```bash
python3 run_tests.py
```

### Using Python's unittest module:
```bash
python3 -m unittest test_calculator.py -v
```

### Running specific test methods:
```bash
python3 -m unittest test_calculator.TestCalculator.test_addition -v
```

## Features Demonstrated

- Unit testing with Python's unittest framework
- Test fixtures using setUp method
- Testing normal cases and edge cases
- Exception testing
- Floating-point comparison with assertAlmostEqual
- Custom test runner with summary statistics

## Test Coverage

The test suite covers:
- Addition, subtraction, multiplication, division operations
- Power/exponentiation operations
- Even number detection
- Error handling (division by zero)
- Edge cases (negative numbers, zero, decimals)
 
