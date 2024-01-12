import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"].to_list())
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # avg = data["temp"].max()
# # print(avg)
# #
# # # To get hold of the row.
# # print(data[data.day == "Monday"])
# # print(data[data.temp == avg])
#
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(monday.temp*9/5 + 32)
#
# # create a data frame from scratch
# data_dict ={
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_as_csv = pandas.DataFrame(data_dict)
data_as_csv.to_csv("squirrel.csv")

