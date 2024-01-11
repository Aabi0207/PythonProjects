import pandas as pd

with open("EnglishVocabulary/data/word_meaning.csv", encoding="utf-8") as file:
    data = file.readlines()

with open("new_data.csv", "w", encoding="utf-8") as new_file:
    for line in data:
        _data = line.split(",")
        new_file.write(_data[0].strip())
        new_file.write(":;")
        new_file.write(_data[1].strip())
        new_file.write(":;")
        new_file.write(",".join(_data[2:]).strip())
        new_file.write("\n")