"""Custom Python functions for use in the project."""

import csv
from typing import Any, Union
import requests
import time

def mini_simple_len(data: list[dict[str, Any]]) -> int:
    """
    Returns the number of records in a list of dictionaries.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a row in the data.
            Example: [{'column1': 'value1', 'column2': 23}, ...]

    Returns:
        int: The number of records in the data.
    """
    count = 0
    for i in data:
        count += 1
    return count

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


def mini_load_csv_dict(input_dict: dict[str, str]) -> list[dict[str, Any]]:
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
    filename = input_dict.get("filename")
    if not filename:
        raise ValueError("Filename is required in the input dictionary.")
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        data = mini_data_types(data)  # Convert data types
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
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row  # TODO Convert data types
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return


def mini_len(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Takes a dictionary with 'Data' and 'Column' keys and returns a dictionary with information about the number of records in a specified column.

    Args:
        input_dict (dict): The input dictionary. Must contain 'Data' and 'Column' keys.
            Example: {"Data": sleep_data, "Column": "sleep"}

    Returns:
        dict[str, Any]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.
            Example: {'Exists': True, 'Column': 'BMI Category', 'NumRecords': 374, 'NumMissing': 0}
    Raises:
        ValueError: If 'Data' or 'Column' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")

    columns = data[0].keys()
    if column in columns:
        missing = 0
        for row in data:
            records = mini_simple_len(data)
            if row[column] in [None, "", "None"]:
                missing += 1
        return {
            "Exists": True,
            "Column": column,
            "NumRecords": records,
            "NumMissing": missing
        }
    else:
        return {"Exists": False}


def mini_search(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Searches for a specific value in a a specific column and returns a dictionary with information about the search result.

    Arg:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.
            Example: {"Data": sleep_data, "Column": "sleep", "Value": "insomnia"}

    Returns:
        dict[str, Any]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.

    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column", "Value"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    search_value = input_dict.get("Value")

    output_dict = {}
    output_dict["Exists"] = False
    for record in data:
        if isinstance(record[column], str):
            if record[column].lower() == search_value.lower():
                output_dict["Exists"] = True
                break
        elif record[column] == search_value:
            output_dict["Exists"] = True
            break

    output_dict["Column"] = column
    output_dict["Value"] = search_value

    return output_dict


def mini_count(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Searches for a specific value in a a specific column and returns a dictionary which contains the proportion of records that match the search value.

    Arg:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.
            Example: {"Data": sleep_data, "Column": "sleep", "Value": "insomnia"}

    Returns:
        dict[str, Any]: A dictionary with keys 'Exists', 'Column', 'Value' and 'Proportion'.
            Example: {'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Proportion': 0.03}
    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column", "Value"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    search_value = input_dict.get("Value")
    output_dict = mini_search(input_dict)
    total = mini_simple_len(data)
    if output_dict["Exists"]:
        count = 0
        for row in data:
            if isinstance(row[column], str):
                if row[column].lower() == search_value.lower():
                    count += 1
            elif row[column] == search_value:
                count += 1
        output_dict["Proportion"] = round(count / total, 2)
    return output_dict  # TODO check if should just be exists


def mini_count_match(input_dict: dict[str, str]) -> dict[str, Any]:
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
    data = input_dict.get("Data")
    conditions = input_dict.copy()
    del conditions["Data"]
    columns = conditions.keys()

    count = 0
    for record in data:
        match = True
        for column in columns:
            if record[column] != input_dict[column]:
                match = False
                break
        if match:  # If all conditions are met
            count += 1

    output_dict = {"Conditions": conditions, "Count": count}
    return output_dict


def mini_average(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Calculates the mean of a specific column in the data.

    Args:
        input_dict (dict): A dictionary containing the data and the column to calculate the mean for.
            Must contain 'Data' and 'Column' keys.
            Example: {"Data": sleep_data, "Column": "Heart Rate"}

    Returns:
        float: The mean of the specified column.

    Raises:
        ValueError: If 'Data' or 'Column' is not provided in the input dictionary.
        ValueError: If the specified column does not contain numeric values.
    """
    mini_validate_input_dict(input_dict, ["Data", "Column"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    
    # Check if column exists in the first record (assuming data is non-empty)
    if not data or column not in data[0]:
        return {"Exists": False, "Column": column}
    
    total = 0.0
    count = 0
    for record in data:
        value = record.get(column)
        if value not in (None, "", "None"):
            if not isinstance(value, (int, float)):
                raise ValueError(f"Column '{column}' does not contain numeric values.")
            total += float(value)
            count += 1
    
    if count == 0:
        average = 0
    else:
        average = round(total / count, 2)
    
    return {"Exists": True, "Column": column, "Average": average}

def mini_extract_metrics(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Takes specified columns and returns a list of dictionaries containing the values for those columns for records where the 'Occupation' is "Teacher".

    Args:
        input_dict (dict[str, str]): A dictionary containing the data and the metrics to extract.
            Must contain 'Data' and 'Metrics' keys.
            Example: {"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep","Col3":"Physical Activity Level"}

    Yields:
        dict: A dictionary with the specified metrics and their values.
            Example: {'Person ID': 262, 'Quality of Sleep': 7, 'Physical Activity Level': 45}

    Raises:
        ValueError: If 'Data' is not provided in the input dictionary.
    """
    mini_validate_input_dict(input_dict, ["Data"])
    data = input_dict.get("Data")
    columns = input_dict.copy()
    del columns["Data"]
    columns = columns.values()
    for record in data:
        if record.get("Occupation") == "Teacher":  
            result = {col: record.get(col, None) for col in columns}
            yield result

def mini_max(data: list[dict[str, Any]], column: str) -> Union[int, float]:
    """
    Returns the maximum value in a specified column of a list of dictionaries.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a row in the data.
            Example: [{'column1': 'value1', 'column2': 23}, ...]

        column (str): The column name to find the maximum value for.
            Example: "Daily Steps"

    Returns:
        int | float: The maximum value found in the specified column.
    """
    max_value = float("-inf")
    for record in data:
        value = record[column]
        if value not in [None, "", "None"] and isinstance(value, (int, float)):
            max_value = max(max_value, value)
    return max_value


def mini_min(data: list[dict[str, Any]], column: str) -> Union[int, float]:
    """
    Returns the minimum value in a specified column of a list of dictionaries.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a row in the data.
            Example: [{'column1': 'value1', 'column2': 23}, ...]

        column (str): The column name to find the minimum value for.
            Example: "Daily Steps"
    Returns:
        int | float: The minimum value found in the specified column.
    """
    min_value = float("-inf")
    for record in data:
        value = record[column]
        if value not in [None, "", "None"] and isinstance(value, (int, float)):
            min_value = max(min_value, value)
    return min_value


def mini_stats(input_dict):
    """
    Takes a dictionary with 'Data', 'Column', and 'Function' keys and returns a dictionary with the result of the specified function (max or min) applied to the specified column.

    Args:
        input_dict (dict): A dictionary containing the data, column, and function to apply.
            Must contain 'Data', 'Column', and 'Function' keys.
            Example: {"Data": sleep_data, "Column": "Age", "Function": "max"}
    Returns:
        dict: A dictionary with the function name, column, and result.
            Example: {'Function': 'max', 'Column': 'Age', 'Result': 65}
    """
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    mini_validate_input_dict(input_dict, ["Data", "Column", "Function"])
    output_dict = {
        "Function": input_dict.get("Function"),
        "Column": column,
    }
    if input_dict.get("Function") == "max":
        output_dict["Result"] = mini_max(data, column)
    elif input_dict.get("Function") == "min":
        output_dict["Result"] = mini_min(data, column)

    return output_dict

def mini_bubble_sort(data: list[dict[str, Any]], column: str) -> dict[str, Any]: #TODO catch non-numerical and maybe change the type hints
    """
    Sorts the values of a specified column in a list of dictionaries using bubble sort.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a record.
            Example: [{'person': 'Alice', 'DailySteps': 200}, {'person': 'Bob', 'DailySteps': 300}]
        column (str): The column name to sort values by.
            Example: "DailySteps"

    Returns:
        dict[str, Any]: A dictionary containing the column name and the sorted list of values.
            Example: {"Column": "DailySteps", "Sorted data": [200, 300]}
    """
    n = mini_simple_len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][column] > data[j + 1][column]:
                data[j], data[j + 1] = data[j + 1], data[j]
    sorted_values = [record[column] for record in data if column in record]

    output_dict = {
        "Column": column,
        "Sorted data": sorted_values
    }
    return output_dict

def mini_value_exists(sorted_data: list[Union[int, float]], value: Union[int, float]):
    """
    Checks if a value exists in a list of data using binary search.
    
    Args: 
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a record.
            Example: [{'person': 'Alice', 'Daily Steps': 200}, {'person': 'Bob', 'Daily Steps': 300}]
        value (int or float): The value to check. 
            Example: 200.
    Returns:
        dict: Of the value searched for and if it exists.
            Example {"Value": 200, "Exists: True}
    """
    left = 0
    right = len(sorted_data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_data[mid]
        
        if mid_value == value:
            return {"Value": value, "Exists": True}
        elif mid_value < value:
            left = mid + 1
        else:
            right = mid - 1
    
    return {"Value": value, "Exists": False}


def mini_frequency_table(input_dict):
    """
    Takes an input dictionary which contains the data and the column to check and returns a frequency table containing the number of times a value appears in the column. 
    """
    mini_validate_input_dict(input_dict, ["Data", "Column"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")
    # TODO add case insensitivity
    
    results = {}
    
    for record in data:
        item = record[column]
        results[item] = results.get(item, 0) + 1
    
    return {column: results}

def mini_call_api_yield(input_dict: dict[str: str]):
    """
    Takes an input dictionary and pulls data from the open-meteo api.
    
    Args:
        input_dict: Input dictionary which includes the city, lat and lon.
            Example: {"city": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060}
    Yields:
        dict: Response data for each city.
            Example: {'latitude': 40.710335, 'longitude': -73.99309, 'generationtime_ms': 0.028967857360839844, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 32.0, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C'}, 'hourly': {'time': ['2025-06-06T00:00'}}.
    """
    url = 'https://api.open-meteo.com/v1/forecast'
    for place in input_dict:
        params = {
            "latitude": place.get("lat"),
            "longitude": place.get("lon"),
            "hourly": "temperature_2m",
        }
        response = requests.get(url, params=params, timeout=1)
        yield response.json()
        time.sleep(1)
        
def mini_call_api_return(input_dict: dict[str: str]):
    """
    Takes an input dictionary and pulls data from the open-meteo api.
    
    Args:
        input_dict: Input dictionary which includes the city, lat and lon.
            Example: {"city": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060}
    Returns:
        list(dict): Response data for each city.
            Example: {'latitude': 40.710335, 'longitude': -73.99309, 'generationtime_ms': 0.028967857360839844, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 32.0, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C'}, 'hourly': {'time': ['2025-06-06T00:00'}}.
    """
    url = 'https://api.open-meteo.com/v1/forecast'
    responses = []
    for place in input_dict:
        params = {
            "latitude": place.get("lat"),
            "longitude": place.get("lon"),
            "hourly": "temperature_2m",
        }
        response = requests.get(url, params=params, timeout=1)
        response_dict = response.json()
        response_dict["city"] = place["city"]
        responses.append(response_dict)
        time.sleep(1)
    return responses

def mini_max_api(data: list[dict[str, Any]]) -> Union[int, float]:
    """
    Returns the maximum value in a specified column of a list of dictionaries.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a row in the data.
            Example: [{'column1': 'value1', 'column2': 23}, ...]

        column (str): The column name to find the maximum value for.
            Example: "Daily Steps"

    Returns:
        int | float: The maximum value found in the specified column.
    """
    max_value = float("-inf")
    for record in data:
        values = record["hourly"]["temperature_2m"]
        for value in values:
            if value > max_value:
                max_value = value
                city = record["city"]
    return {"City": city, "Max temp": max_value}

def mini_min_api(data: list[dict[str, Any]]) -> Union[int, float]:
    """
    Returns the maximum value in a specified column of a list of dictionaries.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a row in the data.
            Example: [{'column1': 'value1', 'column2': 23}, ...]

        column (str): The column name to find the maximum value for.
            Example: "Daily Steps"

    Returns:
        int | float: The maximum value found in the specified column.
    """
    min_value = float("-inf")
    for record in data:
        values = record["hourly"]["temperature_2m"]
        for value in values:
            if value < min_value:
                min_value = value
                city = record["city"]
    return {"City": city, "Max temp": min_value}