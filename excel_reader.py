import pandas as pd
import os

""" Reads the content of an excel file using the Pandas library and displays it in the screen. """

class MyExcel():

    def __init__(self, filename, path = '') -> None:
        self.path = path       # path to the excel file
        self.filename = filename
        self.full_path = os.path.join(path, filename)

    def show_excel(self):
        """ Prints the content of the excel file"""
        df = pd.read_excel(self.full_path)
        print(df)

if __name__ == "__main__":
    e = MyExcel(filename= 'babe_ruth_stats.xlsx')
    e.show_excel()
