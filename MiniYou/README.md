# bbk-bda-project1
--- 
# Part A
Write commments on each data set #TODO
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
### BD1 mini_get_weather_data_yeild
Functions to be used based on their purpose. For streaming the data use yield for sorting/searching etc. use the return function. 
**IO**
*Usage*: 
```
for result in mini_get_weather_data_yield(cities): 
    print(result)
```
*Output:* #TODO

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
weather_data = mini_get_weather_data(cities)
hottest = mini_hottest_city(weather_data)
print(hottest)
```
*Output:* #TODO

**Big-O**
Time: #TODO
Space:  #TODO

**Return or yield**
 #TODO

### D3 mini_get_coldest_city
**IO**
*Usage*:
```
weather_data = mini_get_weather_data(cities)
coldest = mini_coldest_city(weather_data)
print(coldest)
```
*Output:* #TODO

**Big-O**
Time: #TODO
Space:  #TODO

**Return or yield**
 #TODO






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

### XX  xxx
**IO**
*Usage*:
*Output:* 

**Big-O**
Time: 
Space: 



### XX  xxx
**IO**
*Usage*:
*Output:* 

**Big-O**
Time: 
Space: 