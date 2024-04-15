#  File: josephus.py
#  Description: Software project that allows users to explore the World Happiness Index dataset
#  Student Name: Lucas Chiang
#  Student UT EID: lmc4866
#  Partner Name: Travis Welsh
#  Partner UT EID: taw3238
#  Course Name: CS 313E
#  Unique Number: 50775
#  Date Created: April 15th, 2024
#  Date Last Modified: April 15th, 2024
import csv

class stats():
    def __init__(self):
        hash_table = {}
        with open("2019.csv", "r") as data:
            for line in csv.reader(data):
                hash_table[line[1]] = [int(line[0])] + list(map(float, line[2:]))
        print(hash_table["Finland"])





if __name__ == "__main__":
    s = stats()

# Overall rank,Country or region,Score,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption