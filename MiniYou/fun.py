"""Custom Python functions for use in the project."""

import csv
from typing import Any


def mini_validate_input_dict(input_dict: dict[str, str], columns: list[str]) -> None:
    """
    Validates that the input dictionary contains all required keys.

    Args:
        input_dict (dict): The input dictionary to validate.
            Example: {"filename": "myproject/mydata.csv"}
        columns (list): A list of required keys that must be present in the input dictionary.
            Example: ["filename"]

    Raises:
        ValueError: If any of the required keys are missing from the input dictionary.
    """
    for column in columns:
        if column not in input_dict:
            raise ValueError(f"Missing required key: '{column}'")


def mini_data_types(data: list[dict[str, str]]) -> list[dict[str, Any]]:
    """
    Converts string values in a list of dictionaries to appropriate data types (int or float).

    Args:
        data (list[dict[str, str]]): A list of dictionaries where each dictionary represents a row in the CSV file.
            Example: [{'column1': 'value1', 'column2': '23'}, ...]

    Returns:
        list[dict[str, str]]: A list of dictionaries with values converted to int or float where applicable.
            Example: [{'column1': 'value1', 'column2': 23}, ...]
    """
    for record in data:
        for column in record:
            try:
                record[column] = int(record[column])  # Try converting to int first
            except ValueError:
                try:
                    record[column] = float(record[column])  # If int fails, try float
                except ValueError:
                    pass  # If both fail, keep the original value
    return data


def mini_load_csv_dict(input_dict: dict[str, str]) -> list[dict[str, str]]:
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


def mini_load_csv_yield(filename: str) -> dict[str, str]:
    """
    Loads a CSV file and yields each row as a dictionary.

    Args:
        filename (str): The path to the CSV file to be read.
            Example: "myproject/mydata.csv"

    Yields:
        dict: Each row of the CSV file as a dictionary.
            Example: [{'column1': 'value1', 'column2': 'value2'}, ...]

    Raises:
        FileNotFoundErrror: If file is not found.
    """
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return


def mini_len(input_dict: dict[str, str]) -> int:
    """
    Takes a dictionary with 'Data' and 'Column' keys and returns a dictionary with information about the number of records in a specified column.

    Args:
        input_dict (dict): The input dictionary. Must contain 'Data' and 'Column' keys.
            Example: {"Data": sleep_data, "Column": "sleep"}

    Returns:
        dict[str, str]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.

    Raises:
        ValueError: If 'Data' or 'Column' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")

    columns = data[0].keys()
    output_dict = {}
    if column in columns:
        output_dict["Exists"] = True
        records = 0
        missing = 0
        for row in data:
            records += 1
            if row[column] is None or row[column] == "" or row[column] == "None":
                missing += 1
        output_dict["Column"] = column
        output_dict["NumRecords"] = records
        output_dict["NumMissing"] = missing

    else:
        output_dict["Exists"] = False

    return output_dict


def mini_search(input_dict: dict[str, str]) -> dict[str, str]:
    """
    Searches for a specific value in a a specific column and returns a dictionary with information about the search result.

    Arg:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.
            Example: {"Data": sleep_data, "Column": "sleep", "Value": "insomnia"}

    Returns:
        dict[str, str]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.

    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column", "Value"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    search_value = input_dict.get("Value")

    output_dict = {}
    for row in data:
        if row[column].lower() == search_value.lower():
            output_dict["Exists"] = True
            break
        else:
            output_dict["Exists"] = False

    output_dict["Column"] = column
    output_dict["Value"] = search_value

    return output_dict


def mini_count(input_dict: dict[str, str]) -> dict[str, int]:
    """
    Searches for a specific value in a a specific column and returns a dictionary which contains the proportion of records that match the search value.

    Arg:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.
            Example: {"Data": sleep_data, "Column": "sleep", "Value": "insomnia"}

    Returns:
        dict[str, str]: A dictionary with keys 'Exists', 'Column', 'Value' and 'Proportion'.
            Example: {'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Proportion': 0.03}
    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column", "Value"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    search_value = input_dict.get("Value")
    output_dict = mini_search(input_dict)
    if output_dict["Exists"]:
        count = 0
        total = 0
        for row in data:
            total += 1
            if row[column].lower() == search_value.lower():
                count += 1
        output_dict["Proportion"] = round(count / total, 2)
    return output_dict  # TODO check if should just be exists


def mini_count_match(input_dict: dict[str, str]) -> dict[str, int]:
    """
    Counts the number of records that match a specific value in a specific column.

    Args:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.
            Example: {"Data": sleep_data, "Occupation": "Doctor", "BMI Category": "Normal"}

    Returns:
        dict[str, int]: A dictionary with keys 'Exists', 'Column', 'Value', and 'Count'.
            Example: {'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Count': 30}

    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """
