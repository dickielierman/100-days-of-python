import csv
import pandas

# with open('weather_data.csv') as file:
#     days = csv.reader(file)
#     next(days)
#     temperatures = []
#     for day in days:
#         temperatures.append(int(day[1]))
#
#     print(temperatures)

data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()

# temp_list = data.temp.to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(f"The average temperature is {average_temp}")

# series_mean = data.temp.mean()
# print(f"The average temperature is {series_mean}")
#
# highest_temp = data.temp.max()
# print(f"The highest temperature was {highest_temp}")


# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
f = (int(monday.temp) * 9/5) + 32
print(f)
