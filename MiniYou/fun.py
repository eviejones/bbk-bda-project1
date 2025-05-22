"""Custom Python functions for use in the project."""

import csv


def mini_load_csv_dict(input_dict):
    """
    Loads a CSV file into a list of dictionaries.

    Args:
        input_dict (dict): A dictionary containing the filename under the key 'filename'.
        Example: {"filename": "myproject/mydata.csv"}

    Returns:
        list: A list of dictionaries where each dictionary represents a row in the CSV file.
        Example: [{'column1': 'value1', 'column2': 'value2'}, ...]

    Raises:
        ValueError: If 'filename' is not provided in the input dictionary.
    """
    filename = input_dict.get('filename')
    if not filename:
        raise ValueError("Filename is required in the input dictionary.")
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data
