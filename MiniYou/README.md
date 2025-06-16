# bbk-bda-project1
--- 
# Part A
### Sleep data
The sleep dataset has 374 records and 13 columns. The data set is 49% female and 51% male. The average age is 42.18 and the most common occupation is a Nurse. Of these nurses, three have insomnia. 

### Health data
The health dataset has 1000 records and 16 columns. The data set is 48% female and 52% male. The average age is 49.86 and the most common amount of alcohol to drink is 3 units.
---
# Part B
### B1  mini_len
**IO**
If exists:
*Usage:* `mini_len({"Data": sleep_data, "Column": "Sleep Disorder"})`
*Output:* `{'Exists': True, 'Column': 'Sleep Disorder', 'NumRecords': 374, 'NumMissing': 219}`
If doesn't exist:
*Usage:* `mini_len({"Data": sleep_data, "Column": "Sleep Dsorder"})`
*Output:* `{'Exists': False}`

**Big-O**
Time: O(n) - iterates through the data.
Space: O(1) — uses constant amount of space. 

**Return or yield**
Uses return because it is summarising the data. 

### B2  mini_search
**IO**
*Usage*: `mini_search({"Data": sleep_data, "Column": "Sleep Disorder", "Value": "Insomnia"})`
*Output:* `{'Exists': True, 'Column': 'Sleep Disorder', 'Value': 'Insomnia'}`

**Big-O**
Time: O(n) - iterates through the data, n is the number of records.
Space: O(1) — uses constant amount of space, the size of the output_dcit does not change if the data increases.

**Return or yield**
Uses return because I am returning a summary of the search. 


### B3 mini_count
**IO**
*Usage*: `mini_count({"Data": sleep_data, "Column": "BMI Category", "Value": "Obese"})`
*Output:* `{'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Proportion': 0.03}`

**Big-O**
Time: O(n) - iterates through the data to count.
Space: O(1) — uses constant amount of space. 

**Return or yield**
Uses return because it summarisies the data. 

### B4  mini_count_match
**IO**
*Usage*: `mini_count_match({"Data": sleep_data, "Occupation": "Doctor", "Heart Rate": 72})`
*Output:* `{'Conditions': {'Occupation': 'Doctor', 'Heart Rate': 72}, 'Count': 25}`

**Big-O**
Time: O(n*m) - n is the rows and m is the conditions.
Space: O(1) - uses constant space.

**Return or yield**
Uses return because it provides a summary.

### B5  mini_average
**IO**
*Usage*: `mini_average(({"Data": sleep_data, "Column": "Daily Steps", "Value": 10000}))`
*Output:* `{'Exists': True, 'Column': 'Daily Steps', 'Value': 10000, 'Average': 6816.84}`

**Big-O**
Time: O(n) - iterates to get sum and count.
Space: O(1) - doesn't create extra space.

**Return or yield**
Return because it is summarising the data. 

### B6  mini_extract_metrics
**IO**
*Usage*: 
```
for teacher in mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep","Col3":"Physical Activity Level"}):
    print(teacher)
```
*Output:* `[{'Person ID': 262, 'Quality of Sleep': 7, 'Physical Activity Level': 45}, {'Person ID': 263, 'Quality of Sleep': 7, 'Physical Activity Level': 45}]`

**Big-O**
Time: O(n*m) - n is the number of rows and m is the columns
Space: O(m) - for the result dictionary that is yielded. Using yield means that there is less memory used in storage as it yields one result at a time, that result depends on the subset with the occupation == teacher condition. 

**Return or yield**
Yield because it is more memory efficient to generate items as needed rather than store all in memory before returning. 

### B7  mini_stats
**IO**
*Usage*: `print(mini_stats({"Data": sleep_data, "Column": "Age", "Function": "max"}))`
*Output:* `print(mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID","Col2":"Quality of Sleep","Col3":"Physical Activity Level"}))`

**Big-O**
Time: O(n) - the time of max and min are O(n) as mentioned below. 
Space: O(1) - doesn't use additional space

**Return or yield**
Return because it is summarising.

### B8  mini_bubble_sort
**IO**
*Usage*: `print(mini_bubble_sort(sleep_data, "Daily Steps"))`
*Output:* `{'Column': 'Daily Steps', 'Sorted data': [3000, 3000, 3000, 3300, 3300, 3500, 3500, 3500, 3700, 3700, 4000, 4000, 4000, 4100, 4100, 4200, 4200, 4800, 4800, 5000, 5000, 5000, 5000, 5000, 5000,]}`

**Big-O**
Time: O(n^2) - due to the nested loop.
Space: O(n) - because of the space used to store the sorted_values, otherwise it would be O(1)

**Return or yield**
Return because you are summarising the data and returning it. 

### B9  mini_value_exists
**IO**
*Usage*: `print(mini_value_exists(sorted_data, 3500))`
*Output:* `{'Value': 3500, 'Exists': True}`

**Big-O**
Time: O(log n) - binary search.
Space: O(1) - uses constant amount of space. 

**Return or yield**
Uses return because it is sumamrising if a value exists. 

### B10  mini_frequency_table
**IO**
*Usage*: `mini_frequency_table({"Data": sleep_data, "Column": "Daily Steps"})`
*Output:* `{'Daily Steps': {3000: 3, 3300: 2}`

**Big-O**
Time: O(n*m) - Needs to process all records. 
Space: O(m) - Where m is the number of unqiue values in the column. 

**Return or yield**
Return because it is processing the data and returning the frequency table. 

---
# Part C
1. Check if the Daily_Steps column exists and how many missing values it contains
```
file_dict = {"filename": "datasets/health_activity_data.csv"}
filename = file_dict["filename"]
health_data = mini_load_csv_dict(file_dict)
print(mini_len({"Data": health_data, "Column": "Daily_Steps"}))`
`{'Exists': True, 'Column': 'Daily_Steps', 'NumRecords': 1000, 'NumMissing': 0}
```

2. Count how many individuals report Daily_Steps of 6457 hours.
`print(mini_count_match({"Data": health_data, "Daily_Steps": 6457}))`
`{'Conditions': {'Daily_Steps': 6457}, 'Count': 1}`

3. Calculate the average BMI across all individuals.
`print(mini_average({"Data": health_data, "Column": "BMI"}))`
`{'Exists': True, 'Column': 'BMI', 'Average': 26.73}`

4. Count how many female users sleep 7.4 hours.
`print(mini_count_match({"Data": health_data, "Gender": "Female", "Hours_of_Sleep": 7.4}))`
`{'Conditions': {'Gender': 'Female', 'Hours_of_Sleep': 7.4}, 'Count': 8}`
---
# Part D
### BD1 mini_get_weather_data_stream
Functions to be used based on their purpose. For streaming the data use yield for sorting/searching etc. use the return function. 
**IO**
*Usage*: 
```
for result in mini_get_weather_data_yield(cities): 
    print(result)
```
*Output Example:*
```
{'latitude': 40.710335, 'longitude': -73.99309, 'generationtime_ms': 0.042438507080078125, 'utc_offset_seconds': 0, 'timezone': 'GMT', 'timezone_abbreviation': 'GMT', 'elevation': 32.0, 'hourly_units': {'time': 'iso8601', 'temperature_2m': '°C'}, 'hourly': {'time': ['2025-06-16T00:00', '2025-06-16T01:00', '2025-06-16T02:00', '2025-06-16T03:00', '2025-06-16T04:00', '2025-06-16T05:00', '2025-06-16T06:00', '2025-06-16T07:00', '2025-06-16T08:00', '2025-06-16T09:00', '2025-06-16T10:00', '2025-06-16T11:00', '2025-06-16T12:00', '2025-06-16T13:00', '2025-06-16T14:00', '2025-06-16T15:00', '2025-06-16T16:00', '2025-06-16T17:00', '2025-06-16T18:00', '2025-06-16T19:00', '2025-06-16T20:00', '2025-06-16T21:00', '2025-06-16T22:00', '2025-06-16T23:00', '2025-06-17T00:00', '2025-06-17T01:00', '2025-06-17T02:00', '2025-06-17T03:00', '2025-06-17T04:00', '2025-06-17T05:00', '2025-06-17T06:00', '2025-06-17T07:00', '2025-06-17T08:00', '2025-06-17T09:00', '2025-06-17T10:00', '2025-06-17T11:00', '2025-06-17T12:00', '2025-06-17T13:00', '2025-06-17T14:00', '2025-06-17T15:00', '2025-06-17T16:00', '2025-06-17T17:00', '2025-06-17T18:00', '2025-06-17T19:00', '2025-06-17T20:00', '2025-06-17T21:00', '2025-06-17T22:00', '2025-06-17T23:00', '2025-06-18T00:00', '2025-06-18T01:00', '2025-06-18T02:00', '2025-06-18T03:00', '2025-06-18T04:00', '2025-06-18T05:00', '2025-06-18T06:00', '2025-06-18T07:00', '2025-06-18T08:00', '2025-06-18T09:00', '2025-06-18T10:00', '2025-06-18T11:00', '2025-06-18T12:00', '2025-06-18T13:00', '2025-06-18T14:00', '2025-06-18T15:00', '2025-06-18T16:00', '2025-06-18T17:00', '2025-06-18T18:00', '2025-06-18T19:00', '2025-06-18T20:00', '2025-06-18T21:00', '2025-06-18T22:00', '2025-06-18T23:00', '2025-06-19T00:00', '2025-06-19T01:00', '2025-06-19T02:00', '2025-06-19T03:00', '2025-06-19T04:00', '2025-06-19T05:00', '2025-06-19T06:00', '2025-06-19T07:00', '2025-06-19T08:00', '2025-06-19T09:00', '2025-06-19T10:00', '2025-06-19T11:00', '2025-06-19T12:00', '2025-06-19T13:00', '2025-06-19T14:00', '2025-06-19T15:00', '2025-06-19T16:00', '2025-06-19T17:00', '2025-06-19T18:00', '2025-06-19T19:00', '2025-06-19T20:00', '2025-06-19T21:00', '2025-06-19T22:00', '2025-06-19T23:00', '2025-06-20T00:00', '2025-06-20T01:00', '2025-06-20T02:00', '2025-06-20T03:00', '2025-06-20T04:00', '2025-06-20T05:00', '2025-06-20T06:00', '2025-06-20T07:00', '2025-06-20T08:00', '2025-06-20T09:00', '2025-06-20T10:00', '2025-06-20T11:00', '2025-06-20T12:00', '2025-06-20T13:00', '2025-06-20T14:00', '2025-06-20T15:00', '2025-06-20T16:00', '2025-06-20T17:00', '2025-06-20T18:00', '2025-06-20T19:00', '2025-06-20T20:00', '2025-06-20T21:00', '2025-06-20T22:00', '2025-06-20T23:00', '2025-06-21T00:00', '2025-06-21T01:00', '2025-06-21T02:00', '2025-06-21T03:00', '2025-06-21T04:00', '2025-06-21T05:00', '2025-06-21T06:00', '2025-06-21T07:00', '2025-06-21T08:00', '2025-06-21T09:00', '2025-06-21T10:00', '2025-06-21T11:00', '2025-06-21T12:00', '2025-06-21T13:00', '2025-06-21T14:00', '2025-06-21T15:00', '2025-06-21T16:00', '2025-06-21T17:00', '2025-06-21T18:00', '2025-06-21T19:00', '2025-06-21T20:00', '2025-06-21T21:00', '2025-06-21T22:00', '2025-06-21T23:00', '2025-06-22T00:00', '2025-06-22T01:00', '2025-06-22T02:00', '2025-06-22T03:00', '2025-06-22T04:00', '2025-06-22T05:00', '2025-06-22T06:00', '2025-06-22T07:00', '2025-06-22T08:00', '2025-06-22T09:00', '2025-06-22T10:00', '2025-06-22T11:00', '2025-06-22T12:00', '2025-06-22T13:00', '2025-06-22T14:00', '2025-06-22T15:00', '2025-06-22T16:00', '2025-06-22T17:00', '2025-06-22T18:00', '2025-06-22T19:00', '2025-06-22T20:00', '2025-06-22T21:00', '2025-06-22T22:00', '2025-06-22T23:00'], 'temperature_2m': [16.6, 15.1, 15.1, 15.1, 15.4, 15.4, 15.1, 15.4, 15.4, 15.5, 15.7, 16.0, 16.2, 16.3, 16.7, 17.9, 18.3, 19.7, 20.7, 22.2, 22.1, 21.9, 21.0, 20.5, 20.0, 19.8, 19.3, 17.5, 17.6, 17.6, 17.5, 17.6, 17.4, 17.2, 17.1, 17.0, 17.2, 17.6, 17.7, 17.8, 18.4, 18.0, 18.1, 18.2, 18.2, 18.0, 18.0, 17.6, 17.7, 17.7, 17.5, 17.5, 17.6, 17.6, 17.9, 19.6, 19.8, 19.7, 19.9, 20.4, 20.6, 22.8, 22.3, 24.6, 26.4, 28.0, 28.8, 28.3, 26.4, 24.5, 24.4, 23.3, 23.2, 22.7, 23.3, 23.2, 22.6, 22.3, 22.2, 22.1, 21.9, 21.7, 21.7, 22.5, 23.7, 25.3, 27.3, 29.1, 30.6, 31.4, 32.2, 32.6, 32.3, 31.7, 31.4, 31.2, 29.6, 23.4, 21.8, 21.9, 22.0, 21.7, 21.5, 21.3, 21.0, 20.7, 20.8, 20.3, 20.6, 21.9, 23.6, 25.0, 26.3, 27.4, 28.4, 29.1, 29.4, 29.1, 27.5, 27.8, 26.5, 25.6, 24.7, 23.8, 23.0, 22.2, 21.4, 20.5, 19.5, 18.9, 18.8, 19.0, 19.6, 20.7, 22.2, 23.6, 24.9, 26.1, 27.0, 27.6, 28.0, 28.0, 27.6, 26.9, 26.1, 25.2, 24.2, 23.3, 22.9, 22.6, 22.3, 21.9, 21.5, 21.3, 21.4, 21.7, 22.4, 23.9, 25.8, 27.5, 28.9, 30.1, 31.0, 31.6, 31.9, 31.9, 31.5, 30.7]}, 'daily_units': {'time': 'iso8601', 'temperature_2m_max': '°C', 'temperature_2m_min': '°C'}, 'daily': {'time': ['2025-06-16', '2025-06-17', '2025-06-18', '2025-06-19', '2025-06-20', '2025-06-21', '2025-06-22'], 'temperature_2m_max': [22.2, 20.0, 28.8, 32.6, 29.6, 28.0, 31.9], 'temperature_2m_min': [15.1, 17.0, 17.5, 21.7, 20.3, 18.8, 21.3]}, 'city': 'New York'}
```

**Big-O**
Time: #TODO
Space:  #TODO

**Return or yield**
 #TODO

### D1 mini_get_weather_data
**IO**
*Usage*: `mini_get_weather_data(cities)`
*Output:* #TODO

**Big-O**
Time: #TODO
Space:  #TODO

**Return or yield**
 #TODO

### D2 mini_get_hottest_city
**IO**
*Usage*:
```
weather_data = list(mini_get_weather_data_stream(cities))
hottest = mini_hottest_city(weather_data)
print(hottest)
```
*Output:* `{'City': 'Madrid', 'Hottest temp': 35.7}`

**Big-O**
Time: O(n) - iterates over all the cities.
Space:  O(1)  - retains the max.

**Return or yield**
Yields the cities and returns the max. 

### D3 mini_get_coldest_city
**IO**
*Usage*:
```
weather_data = list(mini_get_weather_data_stream(cities))
coldest = mini_coldest_city(weather_data)
print(coldest)
```
*Output:* `{'City': 'Sydney', 'Coldest temp': 2.7}`

**Big-O**
Time: O(n) - iterates over all the cities.
Space:  O(1)  - retains the min.

**Return or yield**
Yields the cities and returns the min. 

### D4 mini_temp_between
**IO**
*Usage*:
```
weather_data = list(mini_get_weather_data_stream(cities))
for city in mini_temp_between(weather_data, 20, 30):
    print(city)
```
*Output:*
```
New York
London
Paris
Tokyo
```

**Big-O**
Time: O(n) - iterates over all the cities.
Space:  O(1)  - retains the min.

**Return or yield**
Yields the cities and returns the min. 

### D5 mini_biggest_temp_diff
**IO**
*Usage*:
```
mini_biggest_temp_diff(weather_data)
```
*Output:*
```
[{'city': 'Madrid', 'difference': 15.600000000000001}, {'city': 'Lisbon', 'difference': 14.7}, {'city': 'Rome', 'difference': 13.899999999999999}, {'city': 'Cairo', 'difference': 13.400000000000002}, {'city': 'Sydney', 'difference': 13.0}]
```

**Big-O**
Time: O(n^2) - because of the bubble sort.
Space:  O(1)  - doesn't take up extra space. 

**Return or yield**
Returns the list

---
# Additional Functions

#### mini_simple_len
**IO**
*Usage*: `print(min_simple_len(sleep_data))`
*Output:* `374`

**Big-O**
Time: O(n) - iterates through the list
Space: O(1) - uses a fixed amount of space, regardless of the size of the list.


#### mini_validate_input_dict
**IO**
*Usage*: `mini_validate_input_dict({"Data": sleep_data}, ["Data", "Column"])`
*Output:* `ValueError: Missing required key: 'Column'`

**Big-O**
Time: O(n) - iterates through each data row, n is the number of keys required in the columns list. 
Space: O(1) - does not require additional space.

#### mini_data_types
**IO**
*Usage*: `mini_data_types(sleep_data)`
*Output:* `[{'Person ID': 1, 'Gender': 'Male', 'Age': 27, 'Occupation': 'Software Engineer', 'Sleep Duration': 6, 'Quality of Sleep': 6, 'Physical Activity Level': 42, 'Stress Level': 6, 'BMI Category': 'Overweight'}]`

**Big-O**
Time: O(n*m) - n is the number of dictionaries in the list, m is the number of keys per dictionary.
Space: O(n) - modifies data in place. 

#### mini_min/mini_max
**IO**
*Usage*: `mini_min(sleep_data, "Daily Steps")` or `mini_max(sleep_data, "Daily Steps")`
*Output:* `1000`

**Big-O**
Time: O(n) - iterates through each data row to find max/min.
Space: O(1) - does not require additional space.