# 0x04 - UTF-8 Validation

This project focuses on validating whether a given array of integers represents a valid UTF-8 encoding.

## Overview

In UTF-8 encoding, characters are represented using variable-length byte sequences. Each character can be represented by one to four bytes. This project aims to validate whether a given array of integers follows the rules of UTF-8 encoding.

## Approach

The validation process involves checking each integer in the array and ensuring that it adheres to UTF-8 encoding rules:

1. For a single-byte character, the most significant bit (MSB) must be 0.
2. For a multi-byte character, the first byte starts with a sequence of 1 followed by a sequence of 0s (e.g., 110xxxxx for two-byte characters, 1110xxxx for three-byte characters, etc.), and subsequent bytes start with 10xxxxxx.
3. Subsequent bytes in a multi-byte character must fall within the range of 10xxxxxx.

## Implementation

The validation algorithm parses the array of integers according to the UTF-8 encoding rules. It iterates through the array, checking each integer against the rules mentioned above. If any integer violates the UTF-8 encoding rules, the algorithm returns false; otherwise, it returns true.

## How to Use

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Open the main validation script (`0-validate_utf8.py`) in your preferred text editor.
4. Review the implementation details and understand the validation algorithm.
5. Execute the script with your array of integers as input to validate whether it represents a valid UTF-8 encoding.

## Example Usage

```python
from validUTF8 import is_valid_utf8

# Example array of integers representing UTF-8 encoding
validUTF8 = [197, 130, 1]

# Validate UTF-8 encoding
valid = is_valid_utf8(validUTF8)
print("Is valid UTF-8 encoding:", valid)
