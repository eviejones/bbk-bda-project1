# bbk-bda-project1
## Part A
Write commments on each data set #TODO
## Part B
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

### B2  mini_search
**IO**
*Usage*: `mini_search({"Data": sleep_data, "Column": "Sleep Disorder", "Value": "Insomnia"})`
*Output:* `{'Exists': True, 'Column': 'Sleep Disorder', 'Value': 'Insomnia'}`

**Big-O**
Time: O(n) - iterates through the data.
Space: O(1) — uses constant amount of space. 

**Return or yield**
Uses return because I am returning a summary of the search. 


### B3 mini_count
**IO**
*Usage*: `mini_count({"Data": sleep_data, "Column": "BMI Category", "Value": "Obese"})`
*Output:* `{'Exists': True, 'Column': 'BMI Category', 'Value': 'Obese', 'Proportion': 0.03}`

**Big-O**
Time: O(n) - iterates through the data to count matches
Space: O(1) — uses constant amount of space. 

**Return or yield**


### B4  mini_count_match
**IO**
*Usage*: `mini_count_match({"Data": sleep_data, "Occupation": "Doctor", "Heart Rate": 72})`
*Output:* `{'Conditions': {'Occupation': 'Doctor', 'Heart Rate': 72}, 'Count': 25}`

**Big-O**
Time: O(n*m) - n is the rows and m is the conditions
Space: O(1) - uses constant space

**Return or yield**

### B5  mini_average
**IO**
*Usage*: `mini_average(({"Data": sleep_data, "Column": "Daily Steps", "Value": 10000}))`
*Output:* `{'Exists': True, 'Column': 'Daily Steps', 'Value': 10000, 'Average': 6816.84}`

**Big-O**
Time: O(n) - iterates to get sum and count
Space: O(1) - doesn't create extra space

**Return or yield**

### B6  mini_extract_metrics
**IO**
*Usage*: `mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep","Col3":"Physical Activity Level"})`
*Output:* `[{'Person ID': 262, 'Quality of Sleep': 7, 'Physical Activity Level': 45}, {'Person ID': 263, 'Quality of Sleep': 7, 'Physical Activity Level': 45}]`

**Big-O**
Time: O(n*m) - n is the number of rows and m is the columns
Space: O(k) - size depends on the subset of data because of the occupation == teacher condition. 

**Return or yield**



### Additional Functions
#### mini_validate_input_dict
**IO**
*Usage*: `mini_validate_input_dict({"Data": sleep_data}, ["Data", "Column"])`
*Output:* `ValueError: Missing required key: 'Column'`

**Big-O**
Time: O(n) - iterates through each data row
Space: O(1) - does not require additional space

#### mini_min/mini_max
**IO**
*Usage*: `mini_min(sleep_data, "Daily Steps")` or `mini_max(sleep_data, "Daily Steps")`
*Output:* `1000`

**Big-O**
Time: O(n) - iterates through each data row to find max/min
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