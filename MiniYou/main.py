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

# Information about the dataset
mini_len({"Data": sleep_data, "Column": "Person ID"})
mini_count({"Data": sleep_data, "Column": "Gender", "Value": "Female"})
mini_frequency_table(({"Data": sleep_data, "Column": "Occupation"}))
mini_count_match({"Data": sleep_data, "Occupation": "Nurse", "Sleep Disorder": 'Insomnia'})

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
print(mini_average(({"Data": sleep_data, "Column": "Daily Steps"})))

# Test mini_extract_metrics
for teacher in mini_extract_metrics({"Data": sleep_data, "Col1":"Person ID", "Col2":"Quality of Sleep","Col3":"Physical Activity Level"}):
    print(teacher)
    break # For testing only

# Test mini_bubble_sort
print(mini_bubble_sort(sleep_data, "Daily Steps", False))

# Test mini_value_exists
sorted_data = mini_bubble_sort(sleep_data, "Daily Steps", False)
sorted_data = sorted_data["Sorted data"]
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

# Part D
cities = [
 {"city": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060},
 {"city": "London", "country": "UK", "lat": 51.5074, "lon": -0.1278},
 {"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
 {"city": "Tokyo", "country": "Japan", "lat": 35.6895, "lon": 139.6917},
 {"city": "Sydney", "country": "Australia", "lat": -33.8688, "lon": 151.2093},
 {"city": "Rio de Janeiro", "country": "Brazil", "lat": -22.9068, "lon": -43.1729},
 {"city": "Cape Town", "country": "South Africa", "lat": -33.9249, "lon": 18.4241},
 {"city": "Moscow", "country": "Russia", "lat": 55.7558, "lon": 37.6173},
 {"city": "Beijing", "country": "China", "lat": 39.9042, "lon": 116.4074},
 {"city": "Mumbai", "country": "India", "lat": 19.0760, "lon": 72.8777},
 {"city": "Cairo", "country": "Egypt", "lat": 30.0444, "lon": 31.2357},
 {"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
 {"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
 {"city": "Toronto", "country": "Canada", "lat": 43.6510, "lon": -79.3470},
 {"city": "Dubai", "country": "UAE", "lat": 25.2048, "lon": 55.2708},
 {"city": "Singapore", "country": "Singapore", "lat": 1.3521, "lon": 103.8198},
 {"city": "Mexico City", "country": "Mexico", "lat": 19.4326, "lon": -99.1332},
 {"city": "Buenos Aires", "country": "Argentina", "lat": -34.6037, "lon": -58.3816},
 {"city": "Istanbul", "country": "Turkey", "lat": 41.0082, "lon": 28.9784},
 {"city": "Bangkok", "country": "Thailand", "lat": 13.7563, "lon": 100.5018},
 {"city": "Nairobi", "country": "Kenya", "lat": -1.2921, "lon": 36.8219},
 {"city": "Seoul", "country": "South Korea", "lat": 37.5665, "lon": 126.9780},
 {"city": "San Francisco", "country": "USA", "lat": 37.7749, "lon": -122.4194},
 {"city": "Jakarta", "country": "Indonesia", "lat": -6.2088, "lon": 106.8456},
 {"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
 {"city": "Lisbon", "country": "Portugal", "lat": 38.7169, "lon": -9.1399},
 {"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
 {"city": "Hanoi", "country": "Vietnam", "lat": 21.0285, "lon": 105.8544},
 {"city": "Oslo", "country": "Norway", "lat": 59.9139, "lon": 10.7522},
 {"city": "Lagos", "country": "Nigeria", "lat": 6.5244, "lon": 3.3792}
]

# Test mini_get_weath_data_yield
for result in mini_get_weather_data_stream(cities):
    print(result)
    
# Test hottest and coldest
weather_data = list(mini_get_weather_data_stream(cities))
print(mini_hottest_city(weather_data))
print(mini_coldest_city(weather_data))

# Test mini_temp_between
for result in mini_temp_between(weather_data, 20, 30):
    print(result)
    
# Test mini_biggest_temp_diff
print(mini_biggest_temp_diff(weather_data))