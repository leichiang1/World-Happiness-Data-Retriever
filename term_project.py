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
import pandas as pd

class stats():
    def __init__(self):
        """Loads the data set into a hash table"""
        self.hash_table = {}
        self.variables = ["Overall Rank", "Happiness Score", "GDP Per Capita", "Social Support", 
                          "Healthy Life Expectancy", "Freedom to Make Life Choices", "Generosity", "Perceptions of Corruption"]
        with open("2019.csv", "r") as data:
            csvreader = csv.reader(data)
            next(csvreader)
            for line in csvreader:
                self.hash_table[line[1]] = [int(line[0])] + list(map(float, line[2:]))

        self.main_menu()
    def main_menu(self):
        """Displays the main menu and controls the overall program based on user input"""
        valid_choices = ["0", "1", "2", "3", "4", "5", "6", "7", "Q"]

        print("#########################################################")
        print("Welcome to World Happiness Data Explorer Project")
        print("#########################################################")
        print("Options: (Type in the Corresponding Number to Choose an Option")
        print("0: Display All Data")
        print("1. Search For a Country")
        print("2. Get Mean for a Category")
        print("3. Get Median for a Category")
        print("4. Get Standard Deviation for a Category")
        print("5. Get Top K countries in a Category")
        print("6. Get Bottom K countries in a Category")
        print("7. Display Category Information")
        print("Q. QUIT")
        print("#########################################################")

        while(True):
            user_input = input()
            if user_input not in valid_choices:
                continue

            if user_input == "0":
                print(self.display_all())

            if user_input == "1":
                self.search()
            
            if user_input == "2":
                mean_choices = ["0", "1", "2", "3", "4", "5", "6", "7" "M"]
                print("#########################################################")
                print("Choose a Category to Find Mean (Type Corresponding Number)")
                print("0. Happiness Score")
                print("1. GDP Per Capita")
                print("2. Social Support")
                print("3. Healthy Life Expectancy")
                print("4. Freedom to Make Life Choices")
                print("5. Generosity")
                print("6. Perceptions of Corruption")
                print("M. Main Menu")
                print("#########################################################")
                user_input = input()
                while(True):
                    if user_input not in mean_choices:
                        continue
                    if user_input == "M":
                        self.main_menu()
                    self.get_mean(int(user_input))
            
            if user_input == "3":
                self.get_median()
            
            if user_input == "4":
                self.get_std_dev()
            
            if user_input == "5":
                self.get_top_k()

            if user_input == "6":
                self.get_bottom_k()
            
            if user_input == "7":
                self.display_cat_info()
            
            if user_input == "Q":
                return

    def display_all(self):
        pd.options.display.max_rows = 1000
        pd.set_option('expand_frame_repr', False)
        file = "2019.csv"
        df = pd.read_csv(file)
        pd.options.display.max_columns = len(df.columns)
        return df
    
    def display_cat_info(self):
        pass

    def get_mean(self, index):
        vals = [list_of_values[index] for list_of_values in self.hash_table.values()]
        print()
        print("Mean Value For Category:", sum(vals) / len(self.hash_table))
        print()
        self.main_menu()

    def search(self, country):
        n = 0
        print()
        print(f"Data for {country}\n")
        for i in self.hash_table[country]:
            print(f"{self.variables[n]}: {i}")
            n = n + 1
        return self.hash_table[country]

    def get_median(self):
        pass

    def get_std_dev(self, index):
        vals = [list_of_values[index] for list_of_values in self.hash_table.values()]
        mean = self.get_mean(index)
        return math.sqrt(sum([mean - x for x in vals])/len(self.hash_table))

    def get_top_k(self):
        pass

    def get_bottom_k(self):
        pass

    def merge_sort(self):
        pass

    def merge(self):
        pass

class min_heap():
    pass


class max_heap():
    pass

if __name__ == "__main__":
    s = stats()
