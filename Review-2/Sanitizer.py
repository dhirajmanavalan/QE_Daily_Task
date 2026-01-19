'''Problem 5: Configuration File Sanitizer
An application loads configuration data written in plain text files.
These files often contain comments, duplicated keys, and inconsistent formatting.
Build a processing module that:
Cleans configuration text

Extracts valid key-value pairs

Detects malformed entries using regex

Stores configurations in an optimized structure

The design must avoid unnecessary abstractions and include Pytest cases for malformed inputs.'''

import re

def read_config(lines):
    config = {}   
    errors = []   
    pattern = re.compile(r"(.+)\s*=\s*(.+)")
    line_number = 0
    for line in lines:
        line_number += 1   
        
        line = line.strip()
        
        if line == "" or line.startswith("#"):
            continue

        match = pattern.match(line)

        if match:
            key = match.group(1)
            value = match.group(2)
            config[key] = value   
        else:
            errors.append((line_number, line))  

    return config, errors

lines = [
    "# comment",
    " owner = Dhiraj",
    "place = Chennai",
    "age = 25",
    "abcd ",
    "dhiru",
    "fuuj",
    "names = diensh"]

config, errors = read_config(lines)
print("correct key value:", config)
print("Errors in key value:", errors)