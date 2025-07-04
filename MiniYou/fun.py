"""Custom Python functions for use in the project."""

import csv
from typing import Any, Generator
import requests
import time


def mini_simple_len(data: list) -> int:
    """
    Returns the number of records in a list of dictionaries.

    Args:
        data (list): A list of data to be counted.

    Returns:
        int: The number of items in the data.

    Example:
        mini_simple_len([{'column1': 'value1', 'column2': 23}])
        1
    """
    count = 0
    for i in data:
        count += 1
    return count


def mini_validate_input_dict(input_dict: dict[str, Any], columns: list[str]) -> None:
    """
    Validates that the input dictionary contains all required keys.

    Args:
        input_dict (dict): The input dictionary to validate.
        columns (list): A list of required keys that must be present in the input dictionary.

    Raises:
        ValueError: If any of the required keys are missing from the input dictionary.

    Example:
        mini_validate_input_dict({"filename": "myproject/mydata.csv"}, ["filename"])
        None
    """
    for column in columns:
        if column not in input_dict:
            raise ValueError(f"Missing required key: '{column}'")


def mini_data_types(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Converts string values in a list of dictionaries to appropriate data types (int or float).

    Args:
        data (list[dict[str, str]]): A list of dictionaries where each dictionary represents a row in the CSV file.

    Returns:
        list[dict[str, str]]: A list of dictionaries with values converted to int or float where applicable.

    Example:
        mini_data_types([{'column1': 'value1', 'column2': '23'})
        [{'column1': 'value1', 'column2': 23}]
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

    Returns:
        list: A list of dictionaries where each dictionary represents a row in the CSV file.

    Raises:
        ValueError: If 'filename' is not provided in the input dictionary.

    Example:
        mini_load_csv_dict({"filename": "myproject/mydata.csv"})
    """
    filename = input_dict.get("filename")
    if not filename:
        raise ValueError("Filename is required in the input dictionary.")
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        data = mini_data_types(data)  # Convert data types
    return data


def mini_load_csv_yield(filename: str) -> Generator[dict[str, str], None, None]:
    """
    Loads a CSV file and yields each row as a dictionary.

    Args:
        filename (str): The path to the CSV file to be read.

    Yields:
        dict: Each row of the CSV file as a dictionary.
            Example: [{'column1': 'value1', 'column2': 'value2'}, ...]

    Raises:
        FileNotFoundError: If file is not found.

    Example:
        mini_load_csv_yield({"filename": "myproject/mydata.csv"})
    """
    try:
        with open(filename, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = mini_data_types([row])[0]
                yield data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return


def mini_len(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Takes a dictionary with 'Data' and 'Column' keys and returns a dictionary with information about the number of records in a specified column.

    Args:
        input_dict (dict): The input dictionary. Must contain 'Data' and 'Column' keys.

    Returns:
        dict[str, Any]: A dictionary with keys 'Exists', 'Column', 'NumRecords', and 'NumMissing'.

    Raises:
        ValueError: If 'Data' or 'Column' is not provided in the input dictionary.

    Example:
        mini_len({"Data": sleep_data, "Column": "sleep"})
        {'Exists': True, 'Column': 'BMI Category', 'NumRecords': 374, 'NumMissing': 0}
    """
    mini_validate_input_dict(input_dict, ["Data", "Column"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")

    columns = data[0].keys()
    if column in columns:
        records = mini_simple_len(data)
        missing = 0
        for row in data:
            if row[column] in [None, "", "None"]:
                missing += 1
        return {
            "Exists": True,
            "Column": column,
            "NumRecords": records,
            "NumMissing": missing,
        }
    else:
        return {"Exists": False}


def mini_search(input_dict: dict[str, Any]) -> dict[str, Any]:
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


def mini_count(input_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Searches for a specific value in a a specific column and returns a dictionary which contains the proportion of records that match the search value.

    Arg:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.

    Returns:
        dict[str, Any]: A dictionary with keys 'Exists', 'Column', 'Value' and 'Proportion'.

    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.

    Example:
        mini_count({"Data": sleep_data, "Column": "sleep", "Value": "insomnia"})
        {'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Proportion': 0.03}
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
    return output_dict


def mini_count_match(input_dict: dict[str, str]) -> dict[str, Any]:
    """
    Counts the number of records that match a specific value in a specific column.

    Args:
        input_dict (dict): A dictionary containing the search term and data. Must contain 'Data', 'Column', and 'Value' keys.

    Returns:
        dict[str, int]: A dictionary with keys 'Exists', 'Column', 'Value', and 'Count'.

    Raises:
        ValueError: If 'Data', 'Column' or 'Value' is not provided in the input dictionary.

    Example:
        mini_count_match({"Data": sleep_data, "Occupation": "Doctor", "BMI Category": "Normal"})
        {'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Count': 30}
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


def mini_average(input_dict: dict[str, int | float]) -> dict[str, Any]:
    """
    Calculates the mean of a specific column in the data. This only works for numerical values.

    Args:
        input_dict (dict): A dictionary containing the data and the column to calculate the mean for. Must contain 'Data' and 'Column' keys.

    Returns:
        dict: Containing if the value exists and the average.

    Raises:
        ValueError: If 'Data' or 'Column' is not provided in the input dictionary.
        ValueError: If the specified column does not contain numeric values.

    Example:
        mini_average({"Data": sleep_data, "Column": "Heart Rate"})
        {"Exists": True, "Column": "Heart Rate", "Average": 69}
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


def mini_extract_metrics(input_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Takes specified columns and returns a list of dictionaries containing the values for those columns for records where the 'Occupation' is "Teacher".

    Args:
        input_dict (dict[str, str]): A dictionary containing the data and the metrics to extract.
        Must contain 'Data' and 'Metrics' keys.

    Yields:
        dict: A dictionary with the specified metrics and their values.

    Raises:
        ValueError: If 'Data' is not provided in the input dictionary.

    Example:
        mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep", "Col3": "Physical Activity Level"})
        {'Person ID': 262, 'Quality of Sleep': 7, 'Physical Activity Level': 45}
    """
    mini_validate_input_dict(input_dict, ["Data"])
    data = input_dict.get("Data")
    columns = [v for k, v in input_dict.items() if k != "Data"]
    for record in data:
        if record.get("Occupation") == "Teacher":
            result = {col: record.get(col, None) for col in columns}
            yield result


def mini_max(data: list | dict, column: str = None) -> int | float:
    """
    Function to find the max of either a list or a dictionary.

    Args:
        data: Either list of dicts OR simple list of values
        column: Column name (only needed for list of dicts)

    Returns:
        int | float: the maximum value found.

    Example:
        mini_max([1,2,3], None)
        3
    """
    max_value = float("-inf")

    if column is None:  # Simple list of values
        for value in data:
            if value not in [None, "", "None"] and isinstance(value, (int, float)):
                if value > max_value:
                    max_value = value
    else:  # List of dictionaries
        for record in data:
            value = record[column]
            if value not in [None, "", "None"] and isinstance(value, (int, float)):
                if value > max_value:
                    max_value = value

    return max_value if max_value != float("-inf") else None


def mini_min(data: list | dict, column=None) -> int | float:
    """
    Function to find the min of either a list or a dictionary.

    Args:
        data: Either list of dicts OR simple list of values
        column: Column name (only needed for list of dicts)

    Returns:
        int | float: the minimum value found.

    Example:
        mini_min([1,2,3], None)
        1
    """
    min_value = float("inf")

    if column is None:
        # Simple list of values
        for value in data:
            if value not in [None, "", "None"] and isinstance(value, (int, float)):
                if value < min_value:
                    min_value = value
    else:
        # List of dictionaries
        for record in data:
            value = record[column]
            if value not in [None, "", "None"] and isinstance(value, (int, float)):
                if value < min_value:
                    min_value = value

    return min_value if min_value != float("inf") else None


def mini_stats(input_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Takes a dictionary with 'Data', 'Column', and 'Function' keys and returns a dictionary with the result of the specified function ('max' or 'min') applied to the specified column.

    Args:
        input_dict (dict): A dictionary containing the data, column, and function to apply.
            Must contain 'Data', 'Column', and 'Function' keys.

    Returns:
        dict: A dictionary with the function name, column, and result.

    Raises:
        ValueError: If 'Data', 'Column' and 'Function' are not included as columns.

    Example:
        mini_stats{"Data": sleep_data, "Column": "Age", "Function": "max"}
        {'Function': 'max', 'Column': 'Age', 'Result': 65}
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


def mini_bubble_sort(
    data: list[dict[str, Any]], column: str, inplace: bool = True
) -> dict[str, Any]:
    """
    Sorts the values of a specified column in a list of dictionaries using bubble sort.

    Args:
        data (list[dict[str, Any]]): A list of dictionaries where each dictionary represents a record.
        column (str): The column name to sort values by.
        inplace (bool): If True sorts the data in place, if False returns the sorted list of data.

    Returns:
        dict[str, Any]: A dictionary containing the column name and the sorted list of values.

    Raises:
        ValueError: If the column contains non-numeric values.

    Example:
        mini_bubble_sort([{'person': 'Alice', 'DailySteps': 200}, {'person': 'Bob', 'DailySteps': 300}], 'DailySteps')
        {'Column': 'DailySteps','Sorted data': [{'person': 'Alice', 'DailySteps': 200}, {'person': 'Bob', 'DailySteps': 300}]}
    """

    n = mini_simple_len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if not isinstance(data[j][column], (int, float)):
                raise ValueError(f"Column '{column}' does not contain numeric values.")
            if data[j][column] > data[j + 1][column]:
                data[j], data[j + 1] = data[j + 1], data[j]

    if inplace:
        sorted_data = data  # Sorted list of dicts
    else:
        sorted_data = [
            record[column] for record in data if column in record
        ]  # Sorted list of values

    return {"Column": column, "Sorted data": sorted_data}


def mini_value_exists(
    sorted_data: list[int | float], value: int | float
) -> dict[str, str | bool]:
    """
    Checks if a value exists in a list of data using binary search.

    Args:
        data (list[int, float]]): A list of dictionaries where each dictionary represents a record.
        value (int or float): The value to check.

    Returns:
        dict: Of the value searched for and if it exists.

    Example:
        mini_value_exists([{'person': 'Alice', 'Daily Steps': 200}, {'person': 'Bob', 'Daily Steps': 300}], 200)
        {"Value": 200, "Exists: True}
    """
    left = 0
    right = mini_simple_len(sorted_data) - 1

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


def mini_frequency_table(input_dict: dict[str, str]) -> dict:
    """
    Takes an input dictionary which contains the data and the column to check and returns a frequency table containing the number of times a value appears in the column.

    Args:
        input_dict (dict): Dictionary containing the data and column to check frequencies.

    Returns:
        dict: Containing the column and the frequencies of all occurences in that column.

    Raises:
        ValueError: If 'Data' and 'Column' are not in the input_dict.

    Example:
        mini_frequency_table({"Data": sleep_data, "Column": "Daily Steps"})
        {'Daily Steps': {3000: 3, 3300: 2}
    """
    mini_validate_input_dict(input_dict, ["Data", "Column"])
    data = input_dict.get("Data")
    column = input_dict.get("Column")

    results = {}

    for record in data:
        item = record[column]
        if isinstance(item, str):
            item = item.lower()
        results[item] = results.get(item, 0) + 1

    return {column: results}


def mini_get_weather_data_stream(
    cities: dict[str, Any],
) -> Generator[dict[str, Any], None, None]:
    """
    Takes an input dictionary and pulls current temperature data from the open-meteo api. This function should be used when the data should be streamed.

    Args:
        cities_dict: Input dictionary which includes the city, lat and lon.
            Example: {"city": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060}
        timeperiod: Must be 'hourly' for hourly breakdown of temperatures or 'daily' for min and max per each day.

    Yields:
        dict: Response data for each city as it's retrieved.

    Example:
        mini_get_weather_data_stream([{'city': 'Lagos','country': 'Nigeria','lat': 6.5244,'lon': 3.3792}])
        {'city': 'Lagos','country': 'Nigeria','lat': 6.5244,'lon': 3.3792,'current_temp': 29.2,'today_max': 29.6,'today_min': 25.6}
    """
    url = "https://api.open-meteo.com/v1/forecast"
    for place in cities:
        params = {
            "latitude": place.get("lat"),
            "longitude": place.get("lon"),
            "current": "temperature_2m",
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "forecast_days": 1,
        }
        try:
            response = requests.get(url, params=params, timeout=15)
            response_dict = response.json()
            place["current_temp"] = response_dict["current"]["temperature_2m"]
            place["today_max"] = response_dict["daily"]["temperature_2m_max"][0]
            place["today_min"] = response_dict["daily"]["temperature_2m_min"][0]
            yield place
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {place['city']}: {e}")
            continue
        time.sleep(1)


def mini_hottest_city(weather_data: list[dict]) -> dict[str, str | float]:
    """
    Returns the maximum temperature and city from existing weather data.

    Args:
        weather data(list[dict]): Weather data provided as a list.

    Returns:
        dict: Dictionary with the hottest city and temperature.

    Example:
        weather_data = list(mini_get_weather_data_stream(cities))
        mini_hottest_city(weather_data)
        {'City': 'Madrid', 'Hottest temp': 36.0}

    """
    max_temp = float("-inf")
    hottest_city = None

    for record in weather_data:
        city_max = record["today_max"]
        if city_max is not None and city_max > max_temp:
            max_temp = city_max
            hottest_city = record["city"]

    return {"City": hottest_city, "Hottest temp": max_temp}


def mini_coldest_city(weather_data: list[dict]) -> dict[str, str | float]:
    """
    Returns the maximum value in a specified column of a list of dictionaries.

    Args:
        weather_data (list[dict[str, Any]]): Weather data retrieved from the API.
        column (str): The column name to find the maximum value for.

    Returns:
        int | float: The maximum value found in the specified column.

    Example:
        weather_data = list(mini_get_weather_data_stream(cities))
        mini_coldest_city(weather_data)
        {'City': 'Sydney', 'Coldest temp': 2.7}
    """
    min_temp = float("inf")
    coldest_city = None

    for record in weather_data:
        city_min = record["today_min"]

        if city_min is not None and city_min < min_temp:
            min_temp = city_min
            coldest_city = record["city"]

    return {"City": coldest_city, "Coldest temp": min_temp}


def mini_temp_between(data: list[dict[str, Any]], min: int | float, max: int | float):
    """
    List cities where the temperature is between two numbers.

    Args:
        data (list[dict[str, Any]]): List of weather data returned from the meteo API.
        min: The bottom end of the range to check.
        max: The top end of the range to check.

    Return:
        list[str]: A list of all of the cities that have a temperature between the min and max.

    Example:
        mini_temp_between(weather_data, 20, 30)
        London, Paris
    """
    for record in data:
        value = record["current_temp"]
        if value < max and value > min:
            yield record["city"]


def mini_biggest_temp_diff(data: list[dict[str, Any]]) -> dict[str, str | float]:
    """
    Lists the top five cities with the biggest temperature difference.

    Args:
        data (list[dict[str, Any]]): List of weather data returned from the meteo API.

    Returns:
        dict: Containing the top five cities and their temperature difference.

    """
    for record in data:
        record["temperature_diff"] = round(record["today_max"] - record["today_min"], 2)

    sorted_result = mini_bubble_sort(data, "temperature_diff", True)["Sorted data"]
    top5 = []
    for rec in sorted_result[-5:][::-1]:  # take last 5 and reverse for descending
        top5.append({"city": rec["city"], "difference": rec["temperature_diff"]})
    return top5