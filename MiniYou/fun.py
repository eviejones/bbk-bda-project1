"""Custom Python functions for use in the project."""

import csv


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
    Returns the length of the input dictionary.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        int: The number of key-value pairs in the dictionary.
    """
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    columns = data[0].keys()
    output_dict = {}
    if column in columns:
        output_dict["Exists"] = True
    else:
        output_dict["Exists"] = False
        
    output_dict["Column"] = column
    if not data:
        raise ValueError("Data is required in the input dictionary. Try adding 'data'.")
    if not column:
        raise ValueError("Column name is required in the input dictionary. Try adding 'Column'.")
    
    records = 0
    missing = 0
    for row in data:
        records += 1
        if row[column] is None or row[column] == "" or row[column] == "None":
            missing += 1
    output_dict["NumRecords"] = records
    output_dict["NumMissing"] = missing
    
    return output_dict
    