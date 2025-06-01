from fun import *

file_dict = {"filename": "MiniYou/datasets/sleep_health_and_lifestyle_data.csv"}
filename = file_dict["filename"]

# Test out mini_load_csv_dict
sleep_data = mini_load_csv_dict(file_dict)
print(sleep_data[0])

# Test out mini_load_csv_yield
sleep_data_yield = mini_load_csv_yield(filename)
# for row in sleep_data_yield:
#     print(row)
#     break  # Print only the first row for demonstration

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
print(mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep","Col3":"Physical Activity Level"}))