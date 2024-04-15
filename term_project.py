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
        """Loads the data set into a hash table"""
        self.hash_table = {}
        self.variables = ["Overall Rank", "Happiness Score", "GDP Per Capita", "Social Support", 
                          "Healthy Life Expectancy", "Freedom to Make Life Choices", "Generosity", "Perceptions of Corruption"]
        with open("2019.csv", "r") as data:
            for line in csv.reader(data):
                self.hash_table[line[1]] = [int(line[0])] + list(map(float, line[2:]))

    def main_menu(self):
        """Displays the main menu and controls the overall program based on user input"""
        pass

    def display_all(self):
        pass

    def search(self):
        pass

    def median(self):
        pass

    def std_dev(self):
        pass

    def merge_sort(self):
        pass

class min_heap():
    pass


class max_heap():
    pass

if __name__ == "__main__":
    s = stats()

# Overall rank,Country or region,Score,GDP per capita,Social support,Healthy life expectancy,Freedom to make life choices,Generosity,Perceptions of corruption
