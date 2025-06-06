from fun import *

# Part A

file_dict = {"filename": "MiniYou/datasets/sleep_health_and_lifestyle_data.csv"}
filename = file_dict["filename"]

# Test out mini_load_csv_dict
sleep_data = mini_load_csv_dict(file_dict)
print(sleep_data[0])

# Test out mini_load_csv_yield
sleep_data_yield = mini_load_csv_yield(filename)
for row in sleep_data_yield:
    print(row)
    break  # Print only the first row for demonstration

# Part B
# Test mini_len
print(mini_len({"Data": sleep_data, "Column": "Sleep Disorder"}))

# Test mini_search
print(mini_search({"Data": sleep_data, "Column": "Sleep Disorder", "Value": "Insomnia"}))
print(mini_search({"Data": sleep_data, "Column": "Sleep Disorder", "Value": "Can't sleep"}))

# Test mini_count
print(mini_count({"Data": sleep_data, "Column": "BMI Category", "Value": "Obese"}))
print(mini_count({"Data": sleep_data, "Column": "BMI Category", "Value": "Obeeese"}))

# Test mini_count_match
print(mini_count_match({"Data": sleep_data, "Occupation": "Doctor", "Heart Rate": 72}))

# Test mini_average
print(mini_average(({"Data": sleep_data, "Column": "Daily Steps", "Value": 10000})))

# Test mini_extract_metrics
for teacher in mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep","Col3":"Physical Activity Level"}):
    print(teacher)
    break # For testing only

# Test mini_bubble_sort
print(mini_bubble_sort(sleep_data, "Daily Steps"))

# Test mini_value_exists
sorted_data = mini_bubble_sort(sleep_data, "Daily Steps")
sorted_data = sorted_data.get("Sorted data")
print(mini_value_exists(sorted_data, 3500))

# Test mini_frequency_table
print(mini_frequency_table({"Data": sleep_data, "Column": "Occupation"}))

# Part C
file_dict = {"filename": "MiniYou/datasets/health_activity_data.csv"}
filename = file_dict["filename"]
health_data = mini_load_csv_dict(file_dict)

# Check if the Daily_Steps column exists and how many missing values it contains
print(mini_len({"Data": health_data, "Column": "Daily_Steps"}))

# Count how many individuals report Daily_Steps of 6457 hours.
print(mini_count_match({"Data": health_data, "Daily_Steps": 6457}))

# Calculate the average BMI across all individuals.
print(mini_average({"Data": health_data, "Column": "BMI"}))

# Count how many female users sleep 7.4 hours.
print(mini_count_match({"Data": health_data, "Gender": "Female", "Hours_of_Sleep": 7.4}))