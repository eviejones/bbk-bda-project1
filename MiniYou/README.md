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
Time: 
Space: 

### Additional Functions
#### mini_validate_input_dict
**IO**
*Usage*: `mini_validate_input_dict({"Data": sleep_data}, ["Data", "Column"])`
*Output:* `ValueError: Missing required key: 'Column'`

**Big-O**
Time: O(n) - iterates through each data row
Space: O(1) - does not require additional space


### XX  xxx
**IO**
*Usage*:
*Output:* 

**Big-O**
Time: 
Space: 