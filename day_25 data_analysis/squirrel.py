import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color_gray = data[data["Primary Fur Color"] == "Gray"]
fur_color_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
fur_color_black = data[data["Primary Fur Color"] == "Black"]

total_of_gray_squirrel = len(fur_color_gray)
total_of_cinnamon_squirrel = len(fur_color_cinnamon)
total_of_black_squirrel = len(fur_color_black)


filtered_data = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [total_of_gray_squirrel, total_of_cinnamon_squirrel, total_of_black_squirrel]
}

filter_data_file = pandas.DataFrame(filtered_data)

filter_data_file.to_csv("squirrel_count.csv")


