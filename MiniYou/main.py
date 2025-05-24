from fun import *

file_dict = {"filename": "MiniYou/datasets/sleep_health_and_lifestyle_data.csv"}
filename = file_dict["filename"]

# Test out mini_load_csv_dict
health_data = mini_load_csv_dict(file_dict)
print(health_data[0]) 

# Test out mini_load_csv_yield
health_data_yield = mini_load_csv_yield(filename)
for row in health_data_yield:
    print(row)
    break  # Print only the first row for demonstration

test_dict = {"Data": health_data, "Column": "Sleep Disorder"}
test_len = mini_len(test_dict)
print(test_len)
