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
    Takes a dictionary with 'Data' and 'Column' keys and returns a dictionary with information about the number of records in a specified column.

    Args:
        input_dict (dict): The input dictionary. Must contain 'Data' and 'Column' keys.
            Example: {"Data": health_data, "Column": "sleep"}

    Returns:
        dict[str, str]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.
    
    Raises:
        ValueError: If 'Data' or 'Column' is not provided in the input dictionary.
    """
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    if not data:
        raise ValueError("Data is required in the input dictionary. Try adding 'data'.")
    if not column:
        raise ValueError("Column name is required in the input dictionary. Try adding 'Column'.")
    
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
            Example: {"Data": health_data, "Column": "sleep", "Value": "insomnia"}
            
    Returns:
        dict[str, str]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.
    
    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    search_value = input_dict.get("Value")

    if not data or not column or not search_value:
        missing_keys = []
        if not data:
            missing_keys.append("'Data'")
        if not column:
            missing_keys.append("'Column'")
        if not search_value:
            missing_keys.append("'Value'")
        raise ValueError(f"Missing required keys in the input dictionary: {', '.join(missing_keys)}")
        
    output_dict = {}
    for row in data:
        print(row)
        if row[column].lower() == search_value.lower():
            output_dict["Exists"] = True
            break
        else:
            output_dict["Exists"] = False
    
    output_dict["Column"] = column
    output_dict["Value"] = search_value
    
    return output_dict
    
def mini_count():
    """
    Searches for a specific value in a a specific column and returns a dictionary with information about the search result.
    
    Arg:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.
            Example: {"Data": health_data, "Column": "sleep", "Value": "insomnia"}
            
    Returns:
        dict[str, str]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.
    
    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """

